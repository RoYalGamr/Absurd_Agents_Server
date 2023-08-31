import random
from words import hangman_word_list
hangman_word_list_local = hangman_word_list


def get_word():
    word = random.choice(hangman_word_list_local)
    return word.upper()


def play(word,client_socket):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    client_socket.send(b"Let's play Hangman!\n")
    client_socket.send(f"{display_hangman(tries)}\n".encode())
    client_socket.send(f"guess the word: {word_completion}".encode())
    client_socket.send(b"\n")
    while not guessed and tries > 0:
        client_socket.send(b"Please guess a letter or word: ")
        guess = client_socket.recv(10).decode().strip("\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                client_socket.send(f"You already guessed the letter {guess}\n".encode())
            elif guess not in word:
                client_socket.send(f"{guess} is not in the word.\n".encode())
                tries -= 1
                guessed_letters.append(guess)
            else:
                client_socket.send(f"Good job, {guess} is in the word!\n".encode())
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                client_socket.send(f"You already guessed the word {guess}\n".encode())
            elif guess != word:
                client_socket.send(f"{guess} is not the word.\n".encode())
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            client_socket.send(b"Not a valid guess.\n")
        client_socket.send(f"{display_hangman(tries)}\n".encode())
        client_socket.send(f"guess the word: {word_completion}".encode())
        client_socket.send(b"\n")
    if guessed:
        client_socket.send(b"Congrats, you guessed the word! You win!\n")
    else:
        client_socket.send(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!\n".encode())


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -""",
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -""",
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -""",
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -""",
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -""",
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -""",
                # rope
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -""",
                # initial empty state
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -"""
    ]
    return stages[tries]

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