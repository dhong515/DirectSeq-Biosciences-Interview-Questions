import socket #Importing the socket library
import csv #Importing the csv library

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates an INET, STREAMing socket
connect = client.connect(('127.0.0.1', 19999)) #Binding the port number and the IP address to the server.

#If the connection to the server was successful, return a success message. 
if(connect != -1):
    print("\nClient has successfully connected with server! \nPress CTRL + 'C' to disconnect at any time. \n")

while True:

    csv_file = input("Enter the name of the csv file: ") #Asking user input in a csv file

    #Opening the csv file and reading in the data.
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        next(reader) #Skipping the first row as it usually contains the titles for each of the columns.
        L = []
        
        #For each row, if the row's second element is not a blank space, convert it to a float and append it to the list
        for row in reader:
            if(row[1] != ''):
                element = row[1]
                element = float(element)
                L.append(element)
    
    print("\n List of extracted data from the csv to be sent to the server: ", L, "\n")

    #Encoding the data so that it could be sent to the server
    L = str(L)
    L = L.encode()

    #Below is a line of code for debugging to make sure the size of the data the server received
    #matches the size that was sent from the client.
    #print("The size of the data sent to the server: ", len(L))

    client.send(L) #Sending the data to the server
    from_server = client.recv(100000) #Receiving the data from the server

    #Below is a line of code for debugging to make sure the size of the data the client received
    #matches the size that was sent from the server side.
    #print("\nThe size of the data received from the server: ", len(from_server))

    #Decoding the data from the server
    data = from_server.decode('utf-8')
    data = eval(data)

    #If there was no basecalling data returned from the server, print a message.
    if len(data) == 0:
        print("No Basecallings were found\n")

    #Prints the basecallings data (presented as a list of tuples) received from the server
    else:
        print("List of Basecallings data: ", data, "\n")
client.close