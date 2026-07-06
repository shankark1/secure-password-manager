from auth import authenticate
from database import initialize_database
from models import PasswordManager

def menu():
    print("\nSecure Password Manager")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

def main():
    initialize_database()
    if not authenticate():
        print("Authentication failed.")
        return

    manager = PasswordManager()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            website = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")
            notes = input("Notes: ")
            manager.add_password(website, username, password, notes)

        elif choice == "2":
            for row in manager.get_all():
                print(row)

        elif choice == "3":
            keyword = input("Search: ")
            for row in manager.search(keyword):
                print(row)

        elif choice == "4":
            pid = int(input("Record ID: "))
            manager.delete(pid)

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
