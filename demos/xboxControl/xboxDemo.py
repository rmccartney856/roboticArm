#NAME: main.py
#DATE: 14/06/2019
#AUTH: Ryan McCartney
#DESC: Python function to control a 6DOF robotic arm with an xbox controller.
#COPY: Copyright 2019, All Rights Reserved, Ryan McCartney

from controller import Controller
import json
import time

status = True
ip_address = "192.168.0.105"

#Clear Log File
open('logs/log.txt', 'w').close()

with open('config/config.json') as json_file:  
    config = json.load(json_file)

#Create instance of Arm class
control = Controller(ip_address,config)

while 1:
    while control.arm.connected:
        while control.gamepads > 0:
            control.connectGamepad()
            while status:
                #Get Current Data
                status = control.getGamepadData()
                status = control.mapButtons()
                status = control.mapJoysticks()
            
        time.sleep(1)
        
    if control.arm.connected == False:
        #Poll connecion
        control.arm.checkConnection()
        print("ERROR: Connection lost with robotic arm. Waiting for reconnect...")
        time.sleep(1)