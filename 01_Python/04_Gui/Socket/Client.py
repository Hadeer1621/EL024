
import socket

# Define constants for the server
HOST = '127.0.0.1'  # Server's hostname or IP address
PORT = 12345        # Port to connect to

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print(f"Connected to server at {HOST}:{PORT}")

    try:
        while True:
            # Send message to the server
            message = input("Enter message to send: ")
            if message.lower() == 'exit':
                break
            client.sendall(message.encode())

            # Receive message from the server
            response = client.recv(1024)
            print(f"Received from server: {response.decode()}")
    except KeyboardInterrupt:
        print("Disconnected from server.")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
