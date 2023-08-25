
f1 = open('wordle.txt','r')
wordle_word_list = []
wordledata = f1.readlines()
for i in wordledata:
    wordle_word_list.append(i.strip("\n").upper())


f2 = open('hangman.txt','r')
hangman_word_list = []
hangmandata = f2.readlines()
for i in hangmandata:
    hangman_word_list.append(i.strip("\n").upper())