#Importing the socket library
import socket
import csv

#Importing the thread module
from _thread import *
import threading

def Main():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates an INET, STREAMing socket
    bind = serv.bind(('127.0.0.1', 19999)) #Binding the server to local port 19999 with IP: '127.0.0.1'

    #If the binding to local port 19999 with IP: '127.0.0.1' was successful, return a success message.   
    if bind != -1:
        print("\nSuccessfully binded to local port 19999 with IP: 127.0.0.1. \nPress CTRL + 'C' to disconnect at any time.\n")

    serv.listen(5) #Creates a listener on the port with a backlog of size 5. Increase this number to handle more clients at once.

    while True:
        conn, addr = serv.accept() #Accepts the incoming connection with the client
        print("Successfully connected with a client \n") #Prints a success message
        start_new_thread(threading, (conn,)) #Starting a new thread and returning its identifier

    serv.close

def threading(conn):
    while True:
        data = conn.recv(100000) #Reads the data that the client sends (max data size of 100,000 bytes)

        #Below is a line of code for debugging to make sure the size of the data the server received
        #matches the size that was sent from the client.
        #print("The size of the data received from the client is: ", len(data)) 

        #Prints message if the client has disconnected and breaks out the while loop
        if not data: 
            print("Disconnected from a client!\n")
            break

        #Decoding the data from the client
        data = data.decode('utf-8')
        data = eval(data)

        #Printing the data from the client
        print("List of floats received from a client: ", data, "\n")

        n = len(data)
        ls = []

        #Searching for any basecallings
        for i in range(n-1):
            for j in range(i+1, n):
                diff = abs(data[j] - data[i])
                if abs(329.0525 - diff) <= 1e-6:
                    basecalling = [data[i], data[j], 'A']
                    ls.append(basecalling)
                if abs(305.0413 - diff) <= 1e-6:
                    basecalling = [data[i], data[j], 'C']
                    ls.append(basecalling)
                if abs(345.0474 - diff) <= 1e-6:
                    basecalling = [data[i], data[j], 'G']
                    ls.append(basecalling)
                if abs(306.0253 - diff) <= 1e-6:
                    basecalling = [data[i], data[j], 'U']
                    ls.append(basecalling)

        #Encoding the basecallings data and sending them back to the client
        L = str(ls)
        L = L.encode()
        conn.send(L)

        #Below is a line of code for debugging to make sure the size of the data the client received
        #matches the size that was sent from the server side.
        #print("\nThe size of the data sent to the client: ", len(L))

    conn.close()

if __name__ == '__main__':
    Main()