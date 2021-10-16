# Hangman

import random as rd

WORDS = ["Pig", "Cow", "Horse"]

word = rd.choice(WORDS)
hiddenword = ["_"] * len(word)
guesses = 6
tried = []
  
while "_" in hiddenword and guesses > 0:
  print(*hiddenword)

  guess = input("Your Guess: ").lower().strip()

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
    print("Yes! That's Correct\n")

    for i in range(len(word)):
      if word.lower()[i] == guess: 
        hiddenword[i] = word[i]

    if not "_" in hiddenword:
      print(*hiddenword)

  elif guess == word.lower():
    print("Yes That's The Word!\n")

    for i in range(len(word)):
      hiddenword[i] = word[i]

    if not "_" in hiddenword:
      print(*hiddenword)

  else:
    print("No! That's Incorrect\n")

    guesses -= 1
    if guesses == 1:
      print("You Have 1 Wrong Guess Left!")
    else:
      print(f"You Have {guesses} Wrong Guesses Left.")

  tried.append(guess)

if guesses > 0:
 print("You Won!")
else:
 print("You Lost..")
