import hashlib
import json
import os

FILE = "users.json"


# Load users from file
def load_users():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return {}


# Save users to file
def save_users(users):
    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)


# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Register user
def register():
    users = load_users()

    username = input("Enter username: ")

    if username in users:
        print("Username already exists!")
        return

    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match!")
        return

    users[username] = hash_password(password)
    save_users(users)

    print("Registration successful!")


# Login user
def login():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == hash_password(password):
        print("\nLogin successful!")
        user_menu(username)
    else:
        print("Invalid username or password!")


# Change password
def change_password(username):
    users = load_users()

    old_password = input("Enter old password: ")

    if users[username] != hash_password(old_password):
        print("Incorrect old password!")
        return

    new_password = input("Enter new password: ")
    users[username] = hash_password(new_password)

    save_users(users)

    print("Password changed successfully!")


# User menu
def user_menu(username):
    while True:
        print("\n--- User Menu ---")
        print("1. Change Password")
        print("2. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            change_password(username)

        elif choice == "2":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice!")


# Main menu
def main():
    while True:
        print("\n===== LOGIN & AUTHENTICATION SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice!")


main()
