#Importing the socket library
import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates an INET, STREAMing socket
serv.bind(('127.0.0.1', 9999)) #Connecting the server to local port 9999 with IP: '127.0.0.1'
serv.listen(5) #Creates a listener on the port with a backlog of size 5

while True:
    conn, addr = serv.accept() #Accepts the incoming connection with the client
    print("\nSuccessfully connected with client!") #Prints a success message

    while True:
        data = conn.recv(4096) #Reads the data that the client sends (max data size of 4096 bytes)

        #Prints message if the client has disconnected and breaks out the while loop
        if not data: 
            print("Disconnected from client!")
            break

        #Decoding the data from the client
        data = data.decode('utf-8')
        data1 = eval(data)

        #Printing the data from the client
        print("List of floats received from client: ", data1)

        n = len(data1)
        ls = []

        #Searching for any basecallings
        for i in range(n-1):
            for j in range(i+1, n):
                diff = abs(data1[j] - data1[i])
                if abs(329.0525 - diff) <= 1e-6:
                    basecalling = [data1[i], data1[j], 'A']
                    ls.append(basecalling)
                if abs(305.0413 - diff) <= 1e-6:
                    basecalling = [data1[i], data1[j], 'C']
                    ls.append(basecalling)
                if abs(345.0474 - diff) <= 1e-6:
                    basecalling = [data1[i], data1[j], 'G']
                    ls.append(basecalling)
                if abs(306.0253 - diff) <= 1e-6:
                    basecalling = [data1[i], data1[j], 'U']
                    ls.append(basecalling)

        #Encoding the basecallings data and sending them back to the client
        L = str(ls)
        L = L.encode()
        conn.send(L)