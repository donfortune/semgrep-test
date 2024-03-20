def insecure_function(password):
    if password == "admin":
        print("Access granted!")
    else:
        print("Access denied!")

if __name__ == "__main__":
    user_password = input("Enter the password: ")
    insecure_function(user_password)
