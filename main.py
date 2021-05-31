# Hangman

import random as rd

WORDS = ["Pig", "Cow", "Horse"]
GUESSES = 6
word = rd.choice(words)
hiddenword = ["_"] * len(word)
tried = []
  
while "_" in hiddenword and guesses > 0:
  print(*hiddenword)
  guess = input("Your Guess: ")
  guess = guess.lower().strip()

  if len(guess) != 1 and len(guess) != len(word):
    print("That Guess is Invalid!")
    continue

  if not guess.isalpha() or not len(guess) in [1, len(word)]:
    print("That Guess is Invalid!\n")
    continue

  if guess in tried: 
    print("You Tried That Already!\n")
    continue

  if len(guess) == 1 and guess in word.lower():
    for x in range(len(word)):
      if word.lower()[x] == guess: 
        hiddenword[x] = word[x]
    print("Yes! That's Correct\n")
    if not "_" in hiddenword: print(*hiddenword)

  elif guess == word.lower():
    for x in range(len(word)): 
      hiddenword[x] = word[x]
    print("Yes That's The Word!\n")
    if not "_" in hiddenword: print(*hiddenword)

  else:
    guesses -= 1
    print("No! That's Incorrect\n")
    if guesses == 1: print("You Have 1 Wrong Guess Left!")
    else: print(f"You Have {guesses} Wrong Guesses Left.")

  tried.append(guess)

if guesses > 0: print("You Won!")
else: print("You Lost..")
