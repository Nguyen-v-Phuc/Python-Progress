import logging
import json

logging.basicConfig(level=logging.INFO, filename="log_users.txt", filemode="a",
                   format="%(asctime)s - %(levelname)s - %(message)s")

#logging.debug("Debug")
#logging.info("User logged in")
#logging.warning("Warning")
#logging.error("Database failed")
#logging.critical("Critical")

def menu():
    while True:
        print("1. Sign in")
        print("2. Sign up")
        print("3. exit")
        print("4. load (only for developer)")

        try:
            choice = int(input("Choose: "))
        except ValueError:
            print("Invalid input")
            continue

        if choice == 1:
            sign_in()
        elif choice == 2:
            sign_up()
        elif choice == 3:
            break
        elif choice == 4:
            load()
        else:
            print("Invalid")

def save(users):
    with open("users-infos-json.json", "w") as file:
        json.dump(users, file, indent=4)

def sign_up():
    users = load()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if not username or not password:
        print("Username and password cannot be empty")
        return

    if username in users:
        print("Username already existed")
        return

    users[username] = password
    save(users)
    print("Sign up successful")
    logging.info(f"{username} signed up")

#status: Done
def sign_in():
    users = load()
    tries = 0

    while tries < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print("Login successful")
            logging.info(f"{username} signed in")
            return
        else:
            print("Login unsuccessful")
            tries += 1
    print("Locked")
    logging.warning(f"An intruder tried to log into {username}'s account")
    return 0

#DON'T TOUCH
def load():
    try:
        with open("users-infos-json.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        logging.error("Can't find file")
        return {}

def main():
    menu()

if __name__ == "__main__":
    main()
