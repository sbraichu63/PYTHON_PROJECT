MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
def deposit():
    while True:
        amount = int(input("Enter the amount you would like to deposit: $"))
        if amount > 0:
            print("Thank you for depostion")
            break
        else:
            print("Enter a valid number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on(1-" + str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")

        else:
            print("Please enter a number")

    return lines

def get_bet():
     while True:
       amount= input("What would you like to bet on each lines? $")
       if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a valid amount between ${MIN_BET} - ${MAX_BET}")

       else:
            print("Please enter a number")
     return amount


       
        
def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet_amount = get_bet() 
    total_amount = bet_amount * lines
    print(f"Your's current balance is : ${balance} ")
    if total_amount <= balance:
     print(f"The amount you are betting is ${bet_amount} on {lines} number of lines and the total amount to be betted is {total_amount}")
    else:
        print("Total amount exceeds the deposit amount \n Please enter a valid amount")

main()

    
