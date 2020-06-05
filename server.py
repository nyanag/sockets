import socket
import pickle

# Initializations
TCP_IP = '127.0.0.1'
TCP_PORT = 2000
BUFFER_SIZE = 1024

#Get user details
# name = input('Enter your name - ')
# card_no = input('Enter your card number - ')
# pin = input('Enter your pin - ')
# balance = input('Enter your balance - ')

name = "Ananya"
card_no = "123"
pin = "123"
balance = "2200"

#Writing data to the database
data = {'Name': name, 'Card_no': card_no, 'Pin': pin, 'Balance': balance}
database = open("db.txt", "a+")
database.write(repr(data)+"\n")

# 1. Create socket: Use IPv4 and Stream Socket (a TCP protocol for data transmission)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. Bind socket to a particular port number and IP address
server_socket.bind((TCP_IP, TCP_PORT))
# 3. Declare willingness to accept incoming connections. Queue up as many as 5 connect requests
server_socket.listen(5)
# 4. Accept an incoming connection request. Create a new socket for this connection
conn, addr = server_socket.accept()
print("Connection address: {}".format(addr[0]))



while 1:

    # 5. Recieve data from socket
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    # Decode message from UTF-8 to Unicode (string)
    sent = pickle.loads(data)

    if sent["c"] == card_no and sent["p"] == pin:
        msg = "Verified"
    else:
        msg = "Not verified"
    # 6. Send data to socket
    msg = msg.encode()
    conn.send(msg)

    data1 = conn.recv(BUFFER_SIZE)
    data1 = data1.decode()

    # print(data1)
    # 
    if int(data1) > int(balance): 
        msg1 = "Oops! Cannot withdraw"
    else:
        r = int(balance) - int(data1)
        msg1 = "Amount withdrawn successfully, Balance ={} ".format(r) 
    
    msg1 = msg1.encode()
    conn.send(msg1)

    

# 7. Close connection
conn.close()
print("Connection closed")