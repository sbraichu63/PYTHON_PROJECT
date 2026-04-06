import random

while True:
    choice = input("Do you want to roll the dice (Y/N):").upper()
    if choice == 'Y':
     number = int(input("Enter the number of times you want to roll the dice:"))
     count = 0
     for i in range (number):
            count += 1
            print(f"Its rolled for the {count} times")
        
            diel1 = random.randint(1,6)
            diel2 = random.randint(1,6)
            print(f"the number after rolling the dice are {diel1},{diel2}")
         

        
    
    elif choice == "N":
        print("Thanks for giving your time for playing the game")
        break

   
    else:
        print("The option you chose was envalid")

