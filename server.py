# Libraries
import socket
import os


# Listen for messages from the client, analyze the data and finally store the data in a log-file - rinse repeat.
def sensor_receive():
    while True:
        sensorData = CSOCKET.recv(1024)
        print(sensorData)

        if sensorData.decode("utf-8") == "exit":
            break


# Accept client and start the loop of receiving data.
def main():
    global CSOCKET
    
    # Listen and connect to a client.
    SSOCKET.bind((SRVIP, PORT))
    os.system('cls')
    print('Listening for a connection...')
    SSOCKET.listen(1)
    CSOCKET, address = SSOCKET.accept()
    print(f'Established a connection to: {address[0]}\n')

    # Start listening for messages.
    sensor_receive()
    SSOCKET.close()


# Initialization: global variables.
PORT = 17123
HFLAGTIME = 20
UTF8 = 'utf-8'

# Initialization: global variables - sockets.
CSOCKET = ''
SSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP-Stream
SRVIP = socket.gethostname()

# Start the program.
main()  
