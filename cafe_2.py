meanu = {
    'tea': 20,
    'cofee': 30,
    'cold drinks': 60,
    "stuffed paratha": 70,
    'roti sabji': 60,
    'burger': 80,
    'pizza': 130,
    'cutlet': 40,
    'pav bhaji': 80
}

def take_orders(meanu):
    total = 0
    orders = []
    while True:
        order = input("What would you like to order? ('q' to finish): ").lower()
        if order == 'q':
            break
        elif order in meanu:
            print("Your order is getting ready")
            total += meanu[order]
            orders.append(order)
        else:
            print("Sorry, that item is not on the menu.")
    return total,orders

total,orders = take_orders(meanu)
print("your orders are:",','.join(orders))
print(f"The total amount to be paid is:{total}")
print("thank you for coming😊")