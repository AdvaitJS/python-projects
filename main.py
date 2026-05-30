import json 
 

file_name = "passwords.json"


def load_passwords():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_password(passwords):
    with open(file_name , 'w') as file:
        json.dump(passwords , file , indent=4)

def add_pass(passwords):
    app = input("Enter site/app name: ")
    password = input("Enter password: ")

    if app in passwords:
        print("Entry already exists")
        return
    passwords[app] = password
    save_password(passwords)
    print("Password saved!")

def search_pass(passwords):
    if not passwords:
        print("Nothing stored yet")
        return 
    app = input("Enter site/app name: ")
    if app not in passwords:
        print("Entry does not exist")
        return
    print(f"Password : {passwords[app]}")

def del_pass(passwords):
    if not passwords:
        print("Nothing stored yet")
        return 
    app = input("Enter app/site name: ")
    if app not in passwords:
        print("Entry doesn't exist")
        return 
    del passwords[app]
    save_password(passwords)
    print("Password deleted successfully")


def view_all(passwords):
    if not passwords:
        print("Nothing stored yet!")
        return 
    for app in passwords:
        print(app)


def main():
    passwords = load_passwords()

    while True:
        print("\n1. Add Password")
        print("2. Search Password")
        print("3. Delete Password")
        print("4. View All Sites")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_pass(passwords)

        elif choice == "2":
            search_pass(passwords)

        elif choice == "3":
            del_pass(passwords)

        elif choice == "4":
            view_all(passwords)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()