Users/Profiles Login Microservice Version 1.0

This program is a microservice used for validating login information for created users in your program. By sending commands to the microservice from your main program, you can enter Username and Password information for existing users, or create new users. You can then use the logged in user to retrieve their corresponding data from your database into your program. Upon start-up, the microservice will populate an array of existing users objects using data from "users_saved.txt". When the program is terminated, it will write/save each users username and password to the same file.
This microservice uses the .txt file "pipe_profiles.txt" as a communication pipeline between your client program and the microservice itself. 
The Python file profiles.py is the main microservice program used to manage commands sent to it through the text file pipe.
It will read commands from the text file "pipe_profiles.txt".

If your main program is running using Python, the file test_profiles.py contains several functions that you can use to directly interact with the microservice without any extra coding. Calling login_ask() will prompt the user for what they want to do (login to existing user, or create new user), and once the necessary Username and Password values are entered, login_ask() will return a string containing the username that is logged it for you to use to load the correct data into your program.

If you are developing a program in another language, below will explain how you can interact with the microservice file profiles.py. 

0. Begin the microservice program using what ever system you have to run Python. The program will populate its array of users, and then read from the pipe textfile "pipe_profiles.txt" until it is told which mode to enter.
1. TO ENTER "Login existing user mode",
- Write "--1--" to the pipe textfile "pipe_profiles.txt"
- profiles.py will then write "--enter_username--" to the pipe, signifying it is ready to receive a username.
- Write the desired Username to the pipe, and profiles.py will then read it. 
- If that username exists in the array of users loaded, profiles.py will write "--enter_password--" to the pipe, signifying it is ready to receive the Password
- Write the matching Password to the pipe, and profiles.py will then read it.
- If the password matches the one in the user array, profiles.py will write "--success--"
to the pipe.
FAIL STATES:
- If the username cannot be found in the users array, "--user_not_found--" will be written to the pipe.
- If the password read does not match the password in users array, "--password_incorrect--" will be written to the pipe.

2. TO ENTER "Create new user Mode",
- Write "--2--" to the pipe textfile "pipe_profiles.txt"
- profiles.py will then write "--create_username--" to the pipe, signifying it is ready to receive a new username.
- Write the desired new Username to the pipe, and profiles.py will then read it.
- If that username does not exist in the array of users, profiles.py will write "--create_password--" to the pipe, signifying it is ready to receive the new Password.
- Write the new Password to the pipe, and profiles.py will then read it.
- profiles.py will then add a new user containing the new username and password to its collection.
- If it is successful, it will write "--success-create--" to the pipe.
FAIL STATES
- If the new username is in the collection of users, it will write "--existing_user_found--" to the pipe.
- If an error occurs while saving the user, it will write "--failed_create--" to the pipe.

If any of the above FAIL STATES occur within profiles.py, the program will return to its beginning state, waiting to read which mode to enter.

TO QUIT Microservice program:
- When profiles.py is in its beginning state, write "--0--" to the pipe file, profiles.py will then read that and save its users before terminating.


COMMANDS to profiles.py
--1--    = Will enter microservice into login user mode
--2--    = Will enter microservice into create user mode
--0--    = Will save and quit the microservice

COMMANDS from profiles.py
--enter_username--    = written when program is ready to receive Username
--user_not_found--    = written if program cannot find user based off Username
--enter_password--    = written when program is ready to receive Password
--password_incorrect--    = written if Password read is incorrect
--success--    = written if Password read matches
--create_username--    = written when program is ready to receive new Username
--existing_user_found--    = written when program cancels create, because username is taken
--create_password--    = written when program is ready to receive new Password
--success_create--    = written when new user is created
--failed_create--    = written when new user fails to be created

Use these values written to the pipe by the profiles.py to according perform necessary actions.
For example, 
WRITING USERNAME TO PIPE in Python:

    with open("pipe_profiles.txt", "w") as pipe: #open file to write Username
        pipe.write(username)
        pipe.flush()

RECEIVING CONFIRMATION FROM PIPE in Python:

    command = password
    while (command == password):
        time.sleep(2)
        with open("pipe_profiles.txt", "r") as pipe: 
            command = pipe.readline().strip()
        # ensure correct response from Password check
        if (command == "--success--"):
            print("\n[SUCCESS]\n")
            return username

NOTE: It is recommended to add a check to make sure a user cannot make their username and password the same as any of the commands used by the microservice. If they do they, microservice will not work.
NOTE: It is recommended to have code in your program to handle unexpected values written by the Microservice to the pipe, in case signal or something occurs that interrupts reading/writing to the file.
Example:

  if (command != "--enter_username--"):
    print("[ERROR]: Unexpected response\n")
    return "--failed--



UML Diagram

![UML diagram microservice A](https://github.com/user-attachments/assets/6308b571-7f25-4ac9-90d7-d013c400bcb6)
