import string
import random
import json
import os

def load_passwords(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_passwords(filename, password_dic):
    with open(filename, 'w') as file:
        json.dump(password_dic, file)

def generate_password(desired_length, complexity):
    password = ""
    if complexity == "easy":
        while len(password) < desired_length:
            password += random.choice(string.digits + string.ascii_lowercase)
    elif complexity == "medium":
        while len(password) < desired_length:
            password += random.choice(string.ascii_letters + string.digits)
    elif complexity == "hard":
        while len(password) < desired_length:
            password += random.choice(string.ascii_letters + string.punctuation + string.digits)
    else:
        print("Error! Please enter a valid complexity.")
        return None
    return password

def main():
    filename = 'passwords.json'
    password_dic = load_passwords(filename)

    print("                             *****Welcome*****")

    name = input("Enter your name: ")

    if name in password_dic:
        choice = input("Do you want to view previous password(s) or create a new one? (view/new): ").lower()
        if choice == "view":
            print(f"Your previous generated passwords are: {password_dic[name]}")
        elif choice == "new":
            desired_length = int(input("Enter the length of the password to be generated: "))
            complexity = input("Enter the complexity of the password (Easy, Medium, or Hard): ").lower()
            password = generate_password(desired_length, complexity)
            if password:
                print(f"Your Password is {password}")
                password_dic[name].append(password)
        else:
            print("Invalid choice. Please enter 'view' or 'new'.")
    else:
        print("No previous passwords found.")
        desired_length = int(input("Enter the length of the password to be generated: "))
        complexity = input("Enter the complexity of the password (Easy, Medium, or Hard): ").lower()
        password = generate_password(desired_length, complexity)
        if password:
            print(f"Your Password is {password}")
            password_dic[name] = [password]

    save_passwords(filename, password_dic)

if __name__ == "__main__":
    main()
