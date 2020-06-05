import socket
import pickle

# Initializations
TCP_IP = '127.0.0.1'
TCP_PORT = 2000
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
#Get user details
name = input('Enter your name - ')
card_no = input('Enter your card number - ')
pin = input('Enter your pin - ')
balance = input('Enter your balance - ')
ask = input('Do you wish to withdraw? Y/N ')
if(ask == 'Y'):
    withdraw = input('Withdrawal amount - ')

send = {"w":withdraw, "b":balance}
pickleData = pickle.dumps(send)
data = {'Name': name, 'Card_no': card_no, 'Pin': pin, 'Balance': balance}
database = open("db.txt", "a+")
database.write(repr(data)+"\n")


# Encode message string of Unicode format to UTF-8 format (Python uses this by default)
BYTE_MESSAGE = pin.encode()

# 1. Create socket: Use IPv4 and Stream Socket (a TCP protocol for data transmission)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. Establish a connection with server
client_socket.connect((TCP_IP, TCP_PORT))



# 3. Send data to socket
client_socket.send(pickleData)
# 4. Recieve data from socket
data = client_socket.recv(BUFFER_SIZE)
# Decode message from UTF-8 to Unicode
data = data.decode()
# 5. Close the socket
client_socket.close()

print(data)
print("Socket closed")