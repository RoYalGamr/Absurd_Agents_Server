import random
from collections import Counter
from words import wordle_word_list
wordle_word_list_local = wordle_word_list

instructions = """Evil Wordle is a single player game 
A player has to guess a five letter hidden word
Try your best !!!
Your Progress Guide "$XX$?"  
"$" Indicates that the letter at that position was guessed correctly 
"?" indicates that the letter at that position is in the hidden word, but in a different position 
"X" indicates that the letter at that position is wrong, and isn't in the hidden word \n"""

def check_valid_guess(guess, word_length, valid_words):
    # Checks if the guess is agreeing with the set of valid words till now
    # i.e. that the 
    return len(guess) == word_length and guess.isalpha() and guess in wordle_word_list_local

def compare_guess_score(guess, matchword):
    score_st = ''
    for i, cur_char in enumerate(guess):
        if cur_char == matchword[i]:
            score_st += '2'
        elif cur_char in matchword:
            score_st += '1'
        else:
            score_st += '0'

    return score_st

def compare_all_scores(guess, valid_words):
    scores = [compare_guess_score(guess, word) for word in valid_words]
    # print("_________________________")
    # print(guess)
    # for word, st in zip(valid_words, scores):
    #     print(word, st)
    # print("_________________________")
    #We find that mask which holds for the maximum number of possible words 
    # And set our set of valid words to all the words which match this mask
    # We break ties with those words which have minimum number of 2's 
    # match_st = max(set(scores), key = scores.count)
    score_counts = Counter(scores)
    
    # Find the maximum occurring score
    max_occurrences = max(score_counts.values())
    most_common_scores = [score for score, count in score_counts.items() if count == max_occurrences]
    
    # Sort the most common scores by the criteria specified
    sorted_most_common_scores = sorted(most_common_scores, key=lambda score: (-score.count('0'), -score.count('1')))
    
    match_st = sorted_most_common_scores[0]
    final_list = [word for word, st in zip(valid_words, scores) if st == match_st]
    return final_list

def play(valid_words,client_socket):
    client_socket.send(instructions.encode())
    word_length = len(valid_words[0])
    
    has_won = False
    guesses = []
    guess_sts = []

    while not has_won:
        #Picks a word at random from the current set of valid words
        client_socket.send(b"Enter your guess: ")
        guess = client_socket.recv(6).decode().strip("\n").upper()

        if check_valid_guess(guess, word_length, valid_words):
            guesses.append(guess)

            valid_words = compare_all_scores(guess, valid_words)
            my_word = random.choice(valid_words)
            comp_st = compare_guess_score(guess, my_word)
            client_socket.send(f"{guess}\n".encode())
            client_socket.send(f"{comp_st.replace('2', '$').replace('1', '?').replace('0', 'X')}\n".encode())
            guess_sts.append(comp_st)

            if comp_st == '2' * word_length:
                has_won = True
                client_socket.send(f"You won in {len(guesses)} {'guess' if len(guesses) == 1 else 'guesses'}!\n".encode())
            else:
                client_socket.send("Incorrect guess. Try again.\n".encode())
        else:
            client_socket.send(f"Invalid guess. Must be {word_length} letters long real English word.\n".encode())

def askplayagain(client_socket):
    client_socket.send(b"Play Again? (Y/N):\n>")
    reply = client_socket.recv(2).decode().strip("\n").upper()
    return reply

def main(client_socket):
    play(wordle_word_list_local,client_socket)
    ans = askplayagain(client_socket)
    while (ans == "Y"):
        play(wordle_word_list_local,client_socket)
        ans = askplayagain(client_socket)

if __name__ == "__main__":
    main()
