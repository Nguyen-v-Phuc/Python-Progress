"""
MÔ TẢ Ý TƯỞNG & CẤU TRÚC CHƯƠNG TRÌNH:
- Ý tưởng: Xây dựng hệ thống đăng nhập/đăng ký bằng Python kết hợp mã hóa bảo mật và ghi log hoạt động.
- Chức năng chính:
  + Bảo mật: Mã hóa mật khẩu bằng bcrypt (salted hashing) trước khi lưu JSON.
  + Lưu trữ: Duy trì dữ liệu người dùng qua file JSON, tự động load/save.
  + Ghi log: Ghi nhật ký đăng ký, đăng nhập và lỗi file vào log_users.txt.
  + Xử lý ngoại lệ: Catch FileNotFoundError khi đọc file dữ liệu.
"""

import logging
import json
import bcrypt

logging.basicConfig(level=logging.INFO, filename="log_users.txt", filemode="a",
                   format="%(asctime)s - %(levelname)s - %(message)s")

#logging.debug("Debug")
#logging.info("User logged in")
#logging.warning("Warning")
#logging.error("Database failed")
#logging.critical("Critical")

def menu():
    while True:
        print("1. Log in")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")

            response = log_in(username, password)
            tries = 0
            while tries < 3:
                response = log_in(username, password)
                print(response)

                if response["status"] == "success":
                    break
                else:
                    tries += 1
                    print(response)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")

            response = register(username, password)
            print(response)
        elif choice == "3":
            break

def save(users):
    with open("users-infos-json.json", "w") as file:
        json.dump(users, file, indent=4)

def register(username, password):
    users = load()

    if not username or not password:
        return {"status": "error", "message": "empty"}

    if username in users:
        return {"status": "error", "message": "username already registered"}

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed.decode()

    save(users)
    logging.info(f"{username} signed up")
    return {"status": "success", "user": username}

#status: Done
def log_in(username, password):
    users = load()
    stored_hash = users[username].encode()

    if username in users and bcrypt.checkpw(password.encode(), stored_hash):
        logging.info(f"{username} signed in")
        return {"status": "success", "user": username}

    else:
        return {"status": "error", "message": "login failed"}

    logging.warning(f"An intruder tried to log into {username}'s account")
    return {"status": "warning", "message": "locked"}
    return

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
