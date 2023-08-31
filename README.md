# Absurd_Agents_Server
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Description
Welcome to our versatile game server that offers a collection of word-based games, including Wordle, Hangman, and their exciting variants. Whether you're a word enthusiast, a strategic thinker, or simply seeking engaging challenges, our server has something for everyone.

The games which are in our service :
- Wordle &ndash; 
Wordle is word puzzle game where players have to guess a hidden five-letter word within six attempts. After each guess, the system provides feedback in the form of symbols ie $,?,X  to indicate correct letters in the right or wrong positions. The objective is to deduce the word through deductive reasoning.its objective is to increase vocablary and word knowledge
- Schrödinger’s cat &ndash;it’s a pretty simple game just you have to guess the box in which the cat hidden among the 5 boxes if you guess correctly you win if you don’t the cat moves to its adjacent box (for ex:- if the cat in box 2 then it either moves to box 1 or box 3 ).this game increases you intelluct and very fun just like rubic's cube
- Hangman &ndash;Hangman is a word guessing game. where systemn genrates a random word and the user tries to guess it by suggesting letters. If the letter is in the word, the user reveals the correct letters in the word. If the letter is not in the word, the player draws a part of a hanged man 
- Dordle &ndash;
 Dordle is a word guessing game that is similar to Wordle, but with a twist. In Dordle, you have to guess two words at the same time, each with five letters. You have seven guesses total, and the letters you guess are used to eliminate letters from both words. To make a guess, type in a five-letter word and press enter.Dordle is a challenging but rewarding game that can help you improve your vocabulary. It is also a lot of fun to try to guess two words at the same time.
- Evilwordle &ndash;
 Evilwordle is a word guessing game that is similar to Wordle, but with a twist. In Evilwordle, the computer is constantly changing the word it is thinking of based on your guesses. This makes the game much more challenging, as you have to be very careful about which letters you guess.f you guess a letter correctly, the computer will change the word it is thinking of to include that letter. However, if you guess a letter incorrectly, the computer will change the word it is thinking of to exclude that letter.the goal of the game is to guess the word that the computer is thinking of in as few guesses as possible.




## Usage

Git clone the repository 
```bash
git clone https://github.com/Ritvik25goyal/Absurd_Agents_Server.git
```
change the working directory to the server
```
cd Absurd_Agents_Server
```


### building Docker file

For Linux Terminal
```bash
docker build . -t servername
```

For Windows (Powershell)
```bash
docker buildx build . -t servername
```

### For running the server
> We have provided the dictionary feature , just change the files in `dictionary` folder and run the server . Dont rename the files .

For Linux terminal
```bash
docker run -p 12345:12345 -v $(pwd)/dictionaries:/app/dictionaries servername
```

For Windows (Powershell)
```bash
docker run -p 12345:12345 -v ${PWD}\dictionaries:/app/dictionaries servername
```
