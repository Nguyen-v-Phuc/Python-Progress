import logging

logging.basicConfig(level=logging.INFO, filename="log_users.txt", filemode="w",
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
            print(users)
        else:
            print("Invalid")


def sign_up():
    users = load()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if not username or not password:
        print("Username and password cannot be empty")
        return 0

    if username in users:
        print("Username already existed")
        return
    with open("users.txt", "a") as file:
        file.write(f"\n{username},{password}")
    print("User signed up")
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
            return 0
        else:
            print("Login unseccessfull")
            tries += 1
    print("Locked")
    logging.warning(f"An intruder tried to log into {username}'s account")
    return 0

#DON'T TOUCH
def load():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                username = username.strip()
                password = password.strip()

                users[username] = password
    except FileNotFoundError:
        logging.error("Can't find file")
        pass
    return users

def main():
    menu()

if __name__ == "__main__":
    main()
