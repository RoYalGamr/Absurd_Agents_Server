
f1 = open('dictionaries/wordle.txt','r')
wordle_word_list = []
wordledata = f1.readlines()
for i in wordledata:
    wordle_word_list.append(i.strip("\n").upper())


f2 = open('dictionaries/hangman.txt','r')
hangman_word_list = []
hangmandata = f2.readlines()
for i in hangmandata:
    hangman_word_list.append(i.strip("\n").upper())