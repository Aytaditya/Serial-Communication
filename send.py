# sending data to firebase

import firebase_admin                                       # type: ignore
from firebase_admin import credentials,db                   # type: ignore
import serial
import time

#Initialize firebase admin sdk with the credentials
cred=credentials.Certificate("path/to/your/credentials.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://your-database.firebaseio.com/'
})

#initialize the serial connection 
ser=serial.Serial(port='COM1', baudrate=9600)  #change the port to the port where your arduino is connected

#reference to the firebase database 
ref=db.reference('sensor')    #change the reference to the path where you want to store the data

#function to send the data to firebase
def send_data_to_firebase(data):
    ref.push().set({     #push the data to the database
        "value":data,    #the data you want to send
        "timestamp":int(time.time())  #the timestamp of the data
    })
    print("Data sent to firebase")

while True:
    if ser.in_waiting:
        #read the data from the serial port
        data=ser.readline().decode('utf-8').strip() #decode the data and remove the trailing newline character

        #send the data to firebase
        send_data_to_firebase(data)

        #wait for 5 seconds before sending the next data
        time.sleep(5)



