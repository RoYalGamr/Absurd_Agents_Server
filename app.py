import socket
import threading
import wordle
import hangman


# Server setup
SERVER_HOST = '172.23.12.209'  # Listen on all available network interfaces
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)  # Listen for up to 5 incoming connections
print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

Instruction = b"Welcome to the server.\n For playing Wordle press W \n For playing Hangman press H \n For exit press Q \n>"

# Handle client 
def handle_client(client_socket, client_address):
    while True:
        client_socket.send(Instruction)
        # Receive data from the client
        data = client_socket.recv(2).decode().strip("\n")
        if data.lower() == "q":
            client_socket.send(b"You have successfully exited.\n")
            break

        # Process player input and send responses
        process_game_input(data,client_socket)  # Implement this function
        # client_socket.send(response.encode())
    client_socket.close()


# Call the function to process player input and generate responses
def process_game_input(input_data,client_socket):
    if input_data.lower() == "w":
        wordle.wordlegame(client_socket)
    if input_data.lower() == "h":
        hangman.main(client_socket)
        

    # return "Response to player input\n"

while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()




