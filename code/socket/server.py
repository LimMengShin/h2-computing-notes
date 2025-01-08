import socket

listen_socket = socket.socket()
listen_socket.bind(("127.0.0.1", 5000))
listen_socket.listen()

chat_socket, addr = listen_socket.accept()

while True:
    data = input("enter data: ").encode()
    chat_socket.sendall(data + b"\n")

    if data == b"quit": break

    print("waiting for client")

    data = b""
    while b"\n" not in data:
        data += chat_socket.recv(1024)
    if data == b"quit\n": break
    
    print(f"client wrote: {data.decode()}")

listen_socket.close()
chat_socket.close()
