def email_slicer():
    email = input("Enter your email address: ")
    index = email.find("@")

    user_name = email[:index]
    domain = email[index + 1:]

    print("Your username is: " + user_name)
    print("Your domain is: " + domain)

def main():
    email_slicer()

if __name__ == "__main__":
    main()

