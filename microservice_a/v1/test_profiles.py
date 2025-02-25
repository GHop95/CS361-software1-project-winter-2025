

import time


def login_user():
    # clear file and write login command --1--
    with open("pipe_profiles.txt", "w") as pipe: 
        pipe.write("--1--")
        pipe.flush()
    # loop and read until login command has changed
    command = "--1--"
    while (command == "--1--"):
        time.sleep(2)
        with open("pipe_profiles.txt", "r") as pipe: #open file to read response
            command = pipe.readline().strip()
        # print("DEBUG: txt read: " + command)
    # ensure correct response from profiles
    if (command != "--enter_username--"):
        print("[ERROR]: Unexpected response\n")
        return "--failed--"
    username = input("Enter Username:\n")
    with open("pipe_profiles.txt", "w") as pipe: #open file to write Username
        pipe.write(username)
        pipe.flush()
    # wait and read Username return message
    command = username
    while (command == username):
        time.sleep(2)
        with open("pipe_profiles.txt", "r") as pipe: #open file to read response from Username search
            command = pipe.readline().strip()
        # print("DEBUG: txt read: " + command)
    # ensure correct response after Profile searches for Username
    if (command == "--user_not_found--"):
        print("\n[ERROR]: No user found\n")
        return "--failed--"
    elif (command != "--enter_password--"):
        print("\n[ERROR]: Unexpected response\n")
        return "--failed--"
    password = input("Enter Password:\n")
    with open("pipe_profiles.txt", "w") as pipe: #open file to write Password
        pipe.write(password)
        pipe.flush()
    command = password
    while (command == password):
        time.sleep(2)
        with open("pipe_profiles.txt", "r") as pipe: #open file to read response from Password check
            command = pipe.readline().strip()
        # print("DEBUG: txt read: " + command)
    # ensure correct response from Password check
    if (command == "--success--"):
        print("\n[SUCCESS]\n")
        return username
    elif (command == "--password_incorrect--"):
        print("\n[ERROR]: Incorrect password\n")
        return "--failed--"
    else:
        print("\n[ERROR]: Unexpected response\n")
        return "--failed--"
    


def create_user():
    # clear file and write create command --2--
    with open("pipe_profiles.txt", "w") as pipe: 
        pipe.write("--2--")
        pipe.flush()
    # loop and read until create command has changed
    command = "--2--"
    while (command == "--2--"):
        time.sleep(2)
        with open("pipe_profiles.txt", "r") as pipe: #open file to read response
            command = pipe.readline().strip()
        # print("DEBUG: txt read: " + command)
    # ensure correct response from profiles
    if (command != "--create_username--"):
        print("[ERROR]: Unexpected response\n")
        return "--failed--"
    new_username = input("Enter new Username:\n")
    with open("pipe_profiles.txt", "w") as pipe: #open file to write new Username
        pipe.write(new_username)
        pipe.flush()
    # wait and read Username return message
    command = new_username
    while (command == new_username):
        time.sleep(2)
        with open("pipe_profiles.txt", "r") as pipe: #open file to read response from new Username search
            command = pipe.readline().strip()
        # print("DEBUG: txt read: " + command)
    # ensure correct response after Profile searches for existing Username
    if (command == "--existing_user_found--"):
        print("\n[ERROR]: Username already exists\n")
        return "--failed--"
    elif (command != "--create_password--"):
        print("\n[ERROR]: Unexpected response\n")
        return "--failed--"
    new_password = input("Enter new Password:\n")
    with open("pipe_profiles.txt", "w") as pipe: #open file to write new Password
        pipe.write(new_password)
        pipe.flush()
    
    command = new_password
    while (command == new_password):
        time.sleep(2)
        with open("pipe_profiles.txt", "r") as pipe: #open file to read response from new Password check
            command = pipe.readline().strip()
        # print("DEBUG: txt read: " + command)
    # ensure correct response user is added
    if (command == "--success_create--"):
        print("\n[SUCCESS]\n")
        return new_username
    elif (command == "--failed_create--"):
        print("\n[ERROR]: failed to save new user\n")
        return "--failed--"
    else:
        print("\n[ERROR]: Unexpected response\n")
        return "--failed--"


def print_login_menu():
    print("""Enter choice:
    1. Login
    2. Create new user
    0. Quit""")


def login_ask():
    passed = 0
    login_choice = -1
    while (passed != 1):
        username = "--failed--"
        print_login_menu()
        login_choice = input()
        if (login_choice == "1"):
            username = login_user()
        elif (login_choice == "2"):
            username = create_user()
        elif (login_choice == "0"):
            with open("pipe_profiles.txt", "w") as pipe: #open file to write Password
                pipe.write("--0--")
                pipe.flush()
            print("Quitting main")
            exit()
        else:
           print("Invalid input.. Try again\n")
        if (username == "--failed--"):
            passed = 0
        else:
            passed = 1
        # End of loop, terminating profiles program
        with open("pipe_profiles.txt", "w") as pipe: #open file to write Password
                pipe.write("--0--")
                pipe.flush()
    return username


def main():
    username = login_ask()
    print("Logged in as: " + username)
    # Proceed to program as user


if __name__ == '__main__':
  main()
