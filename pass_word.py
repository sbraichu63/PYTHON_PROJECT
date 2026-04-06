import random
import string
length = int(input("enter the number of digit you want a password of:"))
all_char = string.ascii_letters + string.digits
password =  "".join(random.choices(all_char, k= length))
print(f"The random password of length {length} is:{password}")