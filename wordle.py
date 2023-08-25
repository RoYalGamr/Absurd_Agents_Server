import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

instructions = """Wordle is a single player game 
A player has to guess a five letter hidden word 
You have six attempts 
Your Progress Guide "$XX$?"  
"$" Indicates that the letter at that position was guessed correctly 
"?" indicates that the letter at that position is in the hidden word, but in a different position 
"X" indicates that the letter at that position is wrong, and isn't in the hidden word"""



def play(word,client_socket):
    client_socket.send(instructions.encode())
    hidden_word = word
    attempt = 6
    while attempt > 0:
        # guess = str(input("Guess the word: "))
        client_socket.send(b"Guess the word: ")
        guess = client_socket.recv(6).decode().strip("\n").upper()
        if guess == hidden_word:
            client_socket.send("You guessed the words correctly! WIN \n".encode())
            break
        else:
            attempt = attempt - 1
            client_socket.send(f"you have {attempt} attempt(s) ,, \n".encode())
            progress = ""
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    #  client_socket.send(f"{word} $ \n".encode())
                    progress += "$"

                elif word in hidden_word:
                    # client_socket.send(f"{word} ? \n".encode())
                    progress += "?"
                else:
                    # client_socket.send(f"{word} X \n".encode())
                    progress += "X"
            client_socket.send(f"{guess}\n".encode())
            client_socket.send(f"{progress}\n".encode())
    if attempt == 0:
        client_socket.send(f"Sorry, you ran out of tries. The word was {hidden_word}. Maybe next time!\n".encode())

def askplayagain(client_socket):
    client_socket.send(b"Play Again? (Y/N):\n>")
    reply = client_socket.recv(2).decode().strip("\n").upper()
    return reply

def main(client_socket):
    word = get_word()
    play(word,client_socket)
    ans = askplayagain(client_socket)
    while (ans == "Y"):
        word = get_word()
        play(word,client_socket)
        ans = askplayagain(client_socket)

if __name__ == "__main__":
    main()