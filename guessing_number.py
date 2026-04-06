import random

number_to_guess = random.randint(1,100)

while True:
    try:
        guess = int(input("Enter the number you guessed:"))
        
        if number_to_guess > guess:
            print(f"{guess} is lower than the required number")

        elif number_to_guess < guess:
            print(f"{guess} is hgiher than the required number")

        else:
            print(f"{guess} is the required number")
            print("Congratulation on wining the lucky draw")
            break

    except:
        print("The number you entered was invalid.\n Please enter the valid number")