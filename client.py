import socket
import pickle

# Initializations
TCP_IP = '127.0.0.1'
TCP_PORT = 2000
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
print('Welcome to the ATM system')
ask = input('Do you wish to withdraw? Y/N ')
if(ask == 'Y'):
    card_no = input('Enter your card number - ')
    pin = input('Enter your pin - ')

#Send data to the socket
send = {"c":card_no, "p":pin}
pickleData = pickle.dumps(send)

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
if data == "Verified":
    print("Your data has been verified!")
    w = input("Enter the amount to withdraw - ")
    wvalue = w.encode()
    client_socket.send(wvalue)
else:
    print("Your data is not verified.")
    
# 4. Recieve data from socket
data1 = client_socket.recv(BUFFER_SIZE)
# Decode message from UTF-8 to Unicode
data1 = data1.decode()
print(data1)

# 5. Close the socket
client_socket.close()

print("Socket closed")