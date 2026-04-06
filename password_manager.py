from cryptography.fernet import Fernet
 

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
'''
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
              user,passw = data.split("|")
              try:
                  decrypt = fer.decrypt(passw.encode()).decode()
                  print("User:",user, "| Password:",decrypt)
              except Exception as e:
                  print(f"Error decrypting password for {user}: {e}")
            else:
                pass

def add():
    name = input("Enter the account name: ")
    pwd = input("The password is: ")

    with open("password.txt","a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

    
while True:
    mode = input("would you like to view the password  or save a new one? (View/Add), press 'q' to quit: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
