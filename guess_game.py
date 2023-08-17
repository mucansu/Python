secret_word = "Giraffe"
guess_limit = 3
out_of_guesses = False
guess = input("Enter guess: ")
guess_count = 1
while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Wrong answer, try again: ")
        guess_count += 1
    else:
        out_of_guesses = True
        print("You have reached max guess")
if guess == secret_word:
    print("Well done!")
