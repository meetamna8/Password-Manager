from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")


def write_key():
    key = Fernet.generate_key()
    with open("key.key" , "wb") as f:
        f.write(key)


write_key()




def view():
    with open('passwords.txt', 'r') as f:
       for line in f.readlines():
           data = (line.rstrip())
           user , passw = data.split("|")
           print(f"user : {user} | password: {passw}")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(f"{name} | {pwd}\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view / add) ? press q to quit. ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode.")
        continue
input()


























