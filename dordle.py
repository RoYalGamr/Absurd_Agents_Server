import random
from words import wordle_word_list
wordle_word_list_local = wordle_word_list

def get_word():
    word = random.choice(wordle_word_list_local)
    return word.upper()

instructions = """----------------------------
        Dordle
----------------------------
Dordle is a single player game
A player has to guess a 2 five letter hidden word with same guess
You have 8 attempts 
Your Progress Guide looks like this "$XX$? | XX$?$"  
"$" Indicates that the letter at that position was guessed correctly 
"?" indicates that the letter at that position is in the hidden word, but in a different position 
"X" indicates that the letter at that position is wrong, and isn't in the hidden word \n"""



def play(client_socket):
    client_socket.send(instructions.encode())
    hidden_word1 = get_word()
    hidden_word2 = get_word()
    print(hidden_word1)
    print(hidden_word2)
    is_solved1 = False
    is_solved2 = False
    attempt = 8
    while attempt > 0:
        client_socket.send(b"Guess the word: ")
        guess = client_socket.recv(6).decode().strip("\n").upper()
        if guess == hidden_word1:
            if is_solved2 :
                client_socket.send("You guessed the both words correctly! WIN \n".encode())
                break
            is_solved1 = True
        if guess == hidden_word2:
            if is_solved1 :
                client_socket.send("You guessed the both words correctly! WIN \n".encode())
                break
            is_solved2 = True
        elif len(guess) == 5:
            attempt = attempt - 1
            client_socket.send(f"you have {attempt} attempt(s) \n".encode())
            progress = ""
            if is_solved1 :
                progress += "$$$$$"
            else:
                for char, word in zip(hidden_word1, guess):
                    if word in hidden_word1 and word in char:
                        progress += "$"
                    elif word in hidden_word1:
                        progress += "?"
                    else:
                        progress += "X"
            progress += " | "
            if is_solved2 :
                progress += "$$$$$"
            else:
                for char, word in zip(hidden_word2, guess):
                    if word in hidden_word2 and word in char:
                        progress += "$"
                    elif word in hidden_word2:
                        progress += "?"
                    else:
                        progress += "X"
            client_socket.send(f"{guess}\n".encode())
            client_socket.send(f"{progress}\n".encode())
        else:
            client_socket.send(b"Not a valid guess.\n")
    if attempt == 0:
        client_socket.send(f"Sorry, you ran out of tries. The words were {hidden_word1} and {hidden_word2}. Maybe next time!\n".encode())

def askplayagain(client_socket):
    client_socket.send(b"Play Again? (Y/N):\n>")
    reply = client_socket.recv(2).decode().strip("\n").upper()
    return reply

def main(client_socket):
    play(client_socket)
    ans = askplayagain(client_socket)
    while (ans == "Y"):
        word = get_word()
        play(client_socket)
        ans = askplayagain(client_socket)

if __name__ == "__main__":
    main()