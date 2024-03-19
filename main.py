import os

def __(user_input):
    os.system("rm -rf " + user_input)

if __name__ == "__main__":
    user_input = input("Enter a file path to delete: ")
    __(user_input)