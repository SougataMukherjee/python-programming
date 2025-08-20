import random

easy_words=["apple","lichi","girl","cap","world"]
medium_word=["python","monkey","banana","laptop"]
hard_word=["elephant","diamond","computer","umbrella"]

print("choose a difficulty level easy medium or hard")

level=input('Enter difficulty').lower()
if level=="easy":
    secret=random.choice(easy_words)
elif level=="medium":
    secret=random.choice(medium_word)
elif level=="hard":
    secret=random.choice(hard_word)
else:
    print("Invalid choice , difficulty to easy level")
    secret=random.choice(easy_words)


attempts=0

print("\n guess the secret password")
while True:
    guess=input("enter your guess").lower()
    attempts += 1

    if guess==secret:
        print(f'congo, you guess it in {attempts} attempts')
        break
    hint=""

    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+="_"
    print("Hint", hint)
print('game over')


