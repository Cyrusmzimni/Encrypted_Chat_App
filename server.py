import socket
import threading


HOST = "127.0.0.1"
PORT = 5555

clients = []


def broadcast(message, sender):
    """Send a message to every connected client except the sender."""
    for client in clients:
        if client != sender:
            try:
                client.sendall(message)
            except OSError:
                remove_client(client)


def remove_client(client):
    """Remove a disconnected client."""
    if client in clients:
        clients.remove(client)

    try:
        client.close()
    except OSError:
        pass


def handle_client(client, address):
    """Handle messages from one connected client."""
    print(f"Client connected: {address}")

    client.sendall(b"Welcome to the Encrypted Chat App!\n")

    while True:
        try:
            message = client.recv(4096)

            if not message:
                break

            print(f"{address}: {message.decode().strip()}")

            broadcast(message, client)

        except (ConnectionResetError, OSError):
            break

    print(f"Client disconnected: {address}")
    remove_client(client)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client, address = server.accept()

        clients.append(client)

        client_thread = threading.Thread(
            target=handle_client,
            args=(client, address),
            daemon=True
        )

        client_thread.start()


if __name__ == "__main__":
    start_server()