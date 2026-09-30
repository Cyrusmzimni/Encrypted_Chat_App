import socket


HOST = "127.0.0.1"
PORT = 5555


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Server listening on {HOST}:{PORT}")

    client_socket, client_address = server.accept()

    print(f"Client connected: {client_address}")

    client_socket.sendall(b"Welcome to the Encrypted Chat App!")

    client_socket.close()
    server.close()


if __name__ == "__main__":
    start_server()