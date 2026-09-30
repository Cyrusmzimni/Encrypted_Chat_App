import socket
import threading


HOST = "127.0.0.1"
PORT = 5555


def receive_messages(client):
    """Receive messages from the server."""
    while True:
        try:
            message = client.recv(4096)

            if not message:
                print("\nDisconnected from server.")
                break

            print(f"\n{message.decode().strip()}")
            print("You: ", end="", flush=True)

        except (ConnectionResetError, OSError):
            print("\nConnection to server lost.")
            break


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((HOST, PORT))

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,),
        daemon=True
    )

    receive_thread.start()

    print("Connected to server.")
    print("Type your messages below.")
    print("Type 'quit' to leave.\n")

    while True:
        try:
            message = input("You: ")

            if message.lower() == "quit":
                break

            if message.strip():
                client.sendall(f"{message}\n".encode())

        except (KeyboardInterrupt, EOFError):
            break

    client.close()
    print("Disconnected.")


if __name__ == "__main__":
    start_client()