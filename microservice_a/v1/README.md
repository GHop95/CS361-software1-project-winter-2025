This is a microservice that uses a txt as a pipe between the client program and the microservice program. It is designed to access and create user logins for your application. The microservice itself is contained in the file profiles.py. Upon start-up, the microservice will populate an array of users containing Usernames and Passwords using data from "users_saved.txt". When the program is terminated, it write/save the arrays contents to the same file.

If your main program is running using Python, the file test_profiles.py contains several functions that you can use to directly interact with the microservice without any extra coding. Calling login_ask() will prompt the user for what they want to do (login to existing user, or create new user), and once the necessary Username and Password values are entered, login_ask() will return a string containing the username that is logged it, for you to use to load the correct data into your program.

If you are using this program with another language, this will explain how you can interact with the microservice file profiles.py. 


0. Begin the program using what ever system you have to run Python. The program will populate its array of users, and then read from the pipe textfile "pipe_profiles.txt" until it is told which mode to enter.
1. To enter "Login existing User Mode",
- Write "--1--" to the pipe textfile "pipe_profiles.txt"
- profiles.py will then write "--enter_username--" to the pipe, signifing it is ready to receive a username.
- Write the desired Username to the pipe, and profiles.py will then read it. 
- If that username exists in the array of users loaded, profiles.py will write "--enter_password--" to the pipe, signifing it is ready to receive the Password
- Write the matching Password to the pipe, and profiles.py will then read it.
- If the password matches the one in the user array, profiles.py will write "--success--"
to the pipe.
FAIL STATES:
- If the username cannot be found in the users array, "--user_not_found--" will be written to the pipe.
- If password read does not match password in users array, "--password_incorrect--" will be written to the pipe.

2. To enter "Login existing User Mode",
- Write "--2--" to the pipe textfile "pipe_profiles.txt"
- profiles.py will then write "--create_username--" to the pipe, signifing it is ready to receive a new username.
- Write the desired new Username to the pipe, and profiles.py will then read it.
- If that username does not exist in the array of users, profiles.py will write "--create_password--" to the pipe, signifing it is ready to receive the new Password.
- Write the new Password to the pipe, and profiles.py will then read it.
- profiles.py will then add a new user containing the new username and password to its collection.
- If it is successful, it will write "--success-create--" to the pipe.
FAIL STATES
- If the new username is in the collection of users, it will write "--existing_user_found--" to the pipe.
- If an error occurs while saving the user, it will write "--failed_create--" to the pipe.

If any of the above FAIL STATES occur within profiles.py, the program will return to its bystanding stage, waiting to read which mode to enter.

Use these values written to the pipe by the profiles.py to according perform necessary actions.

For example, 
WRITING USERNAME TO PIPE in Python:

  with open("pipe_profiles.txt", "w") as pipe: #open file to write Username
    pipe.write(username)
    pipe.flush()

RECIEVING CONFIRMATION FROM PIPE in Python:

  command = password
  while (command == password):
    time.sleep(2)
    with open("pipe_profiles.txt", "r") as pipe: 
      command = pipe.readline().strip()
    # ensure correct response from Password check
    if (command == "--success--"):
      print("\n[SUCCESS]\n")
      return username

NOTE: It is recommended to have code in your program to handle unexpected values written by the Microservice to the pipe, in case something unexpected happens.
Example:

  if (command != "--enter_username--"):
    print("[ERROR]: Unexpected response\n")
    return "--failed--
