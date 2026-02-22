"""
 Lab 6  User Login System
sammy Saqfelhait
This program   for login system using a dictionary to store usernames and passwords. 
It  will checks if the username exists and allows the user up to three password attempts before locking the account.
Date: 02/20/2026"""

from typing import Dict


def main() -> None:
    users: Dict[str, str] = {
        "gwalters": "S3curePass!",
        "admin": "Admin123",
        "jsmith": "Password1",
        "guest": "guest"}
    username: str = input("Enter username: ")

    if username not in users:
        print("\nUser not found. Exiting.")
        return

    attempts: int = 0
    max_attempts: int = 3

    while attempts < max_attempts:
        password: str = input("Enter password: ")

        if password == users[username]:
            if username == "guest":
                security_level: str = "Guest access"
            else:
                security_level = "Security Level 1"

            print(f"\nWelcome, {username}. You have {security_level}.")
            return
        else:
            attempts += 1
            if attempts < max_attempts:
                print("Access Denied. Try again.")
            else:
                print("\nToo many failed attempts. Account locked.")


if __name__ == "__main__":
    main()