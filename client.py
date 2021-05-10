#################################################   Libraries   ########################################################
#!/usr/bin/python3
import os
import time
import socket
import sys
import threading
from datetime import datetime
import RPi.GPIO as GPIO

###############################################   Program Start   ######################################################
# TEXT
def main():
    # Clean terminal output.
    os.system('clear')

    # Connect to the server.
    print('Connecting to server...', end="")
    srvSock.connect((srvIp, port))
    print(' connected!\n')

    # Start sampling sensor data.
    rfidThread.start()
    motionThread.start()


#################################################   Functions   ########################################################
# Continously read the pin 10 and send socket data if a change has occured (made for motion sensor data).
# Structure of packet: [1 byte: Class][1 bytes: 1/0, singnaling motion detected]
def motionRun():
    inputOld = 0
    input = 0

    while True:
        input = GPIO.input(10)
        if input != inputOld:
            #sendSecure("1" + str(input))
            print("Send: " + "1" + str(input))

        # Setup for the next cycle.
        inputOld = input


# Continously wait for input and send in-stream as a socket packet (made for RFID-input).
# Structure of packet: [1 byte: Class][8 bytes: RFID-tag][The rest: Date, down to micro seconds]
def rfidRun():
    while True:
        rfid = input()
        timeNow = datetime.now()
        timestamp = timeNow.strftime("%y%m%d%H%M%S.%f")
        #sendSecure("2" + rfid + timestamp)
        print("Send: " + "2" + rfid + timestamp)


# TEXT
def sendSecure(strArg):
    threadLock.acquire()
    srvSock.send(bytes(strArg, utf8))
    threadLock.release()


##############################################   Global variables    ###################################################
srvIp = socket.gethostname()  # CHANGE
port = 17123
utf8 = 'utf-8'
srvSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN)

threadLock = threading.Lock()
rfidThread = threading.Thread(target=rfidRun)
motionThread = threading.Thread(target=motionRun)

# Start the program.
main()
