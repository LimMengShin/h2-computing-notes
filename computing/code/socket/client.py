import socket

chat_socket = socket.socket()
chat_socket.connect(("127.0.0.1", 5000))

while True:
    data = b""
    while b"\n" not in data:
        data += chat_socket.recv(1024)
    if data == b"quit\n": break
    
    print(f"server wrote: {data.decode()}")

    data = input("enter data: ").encode()
    chat_socket.sendall(data + b"\n")

    if data == b"quit": break

    print("waiting for server")

chat_socket.close()