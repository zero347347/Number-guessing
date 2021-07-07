# we are going to use if, while loop and variables
# while, you need to think which one will continue, if wrong


secret_number = 7
number = float(input("guess_number: "))
guess_count = 0

while (secret_number != number) and (guess_count < 4):
    print("Try it again")
    number = float(input("guess_number: "))
    guess_count += 1
    if guess_count >= 4:
        print("You lose")
if (secret_number == number) and (guess_count < 4):
    print("You guess it correctly")
