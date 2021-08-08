#Importing the socket library
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates an INET, STREAMing socket
connect = client.connect(('127.0.0.1', 9999)) #Connecting the client to local port 9999 with IP: '127.0.0.1'

#If the connection to the server was successful, return a success message. 
if(connect != -1):
    print("\nSuccessfully connected with server! Press CTRL + 'C' to disconnect at any time. \n")

while True:
    #Accepting the the list of floats (Separated by commas) imputted through the terminal from the user
    L = [float(x) for x in input("Enter the list of floats (Separated by commas)\n").split(',')]

    #Encoding the data so that it could be sent to the server
    L = str(L)
    L = L.encode()

    client.send(L) #Sending the data to the server
    from_server = client.recv(4096) #Receiving the data from the server

    #Decoding the data from the server
    data = from_server.decode('utf-8')
    data1 = eval(data)

    #If there was no basecalling data returned from the server, print a message.
    if len(data1) == 0:
        print("No Basecallings were found\n")

    #Prints the basecallings data (presented as a list of tuples) received from the server
    else:
        print("List of Basecallings data: ", data1, "\n")