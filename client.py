import socket


HOST = "127.0.0.1"
PORT = 5555


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((HOST, PORT))

    welcome_message = client.recv(1024).decode()
    print(welcome_message)

    client.close()


if __name__ == "__main__":
    start_client()