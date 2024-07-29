import socket
import threading

# Define constants for the server
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connection established with {client_address}")
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Received from {client_address}: {message.decode()}")
            
            # Echo the message back to the client
            client_socket.sendall(message)
        except ConnectionResetError:
            print(f"Connection lost with {client_address}")
            break

    client_socket.close()
    print(f"Connection closed with {client_address}")

# Main function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
