

print("=== Guessing Game ====")

secret_word = "python"

while True:
    word = input("Guess the Programming language: ").lower()

    if word == secret_word:
        print("You guessed Correct language!!! ")
        break

    else:
        print("Incorrect guess. Try again!!")
        