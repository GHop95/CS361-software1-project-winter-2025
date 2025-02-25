


import time

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password


def login_user_p(users):
	# open file to write ask for Username
	with open("pipe_profiles.txt", "w") as pipe: 
		pipe.write("--enter_username--")
		pipe.flush()
	# open file to read Username
	command = "--enter_username--"
	while (command == "--enter_username--"):
		time.sleep(2)
		with open("pipe_profiles.txt", "r") as pipe: 
			command = pipe.readline().strip()
		print("DEBUG: txt read while waiting for Username: " + command)
	# once username is read, for each username in array compare to command
	user_found = None
	for x in users: 
		if (x.username == command):
			user_found = x
			break
	# end if no match is found
	# open file to write Not Found
	if (user_found == None):
		print("DEBUG: no user found")
		with open("pipe_profiles.txt", "w") as pipe: 
			pipe.write("--user_not_found--")
			pipe.flush()
		print("DEBUG: check pipe NOW for --user_not_found--")
		return
	# clear file and request Password
	print("DEBUG: user found")
	with open("pipe_profiles.txt", "w") as pipe:
		pipe.write("--enter_password--")
		pipe.flush()
	# open file to read Password
	command = "--enter_password--" 
	while (command == "--enter_password--"):
		time.sleep(2)
		with open("pipe_profiles.txt", "r") as pipe: 
			command = pipe.readline().strip()
		print("DEBUG: txt read while waiting for Password: " + command)
	# compare readline to password
	if (user_found.password == command):
		# open file to write Success
		with open("pipe_profiles.txt", "w") as pipe: 
			pipe.write("--success--")
			pipe.flush()
	else:
		# open file to write Incorrect
		with open("pipe_profiles.txt", "w") as pipe: 
			pipe.write("--password_incorrect--")
			pipe.flush()
	return
	

def create_user_p(users):
	# open file to write ask for Username
	with open("pipe_profiles.txt", "w") as pipe: 
		pipe.write("--create_username--")
		pipe.flush()
	# open file to read Username
	command = "--create_username--"
	while (command == "--create_username--"):
		time.sleep(2)
		with open("pipe_profiles.txt", "r") as pipe: 
			command = pipe.readline().strip()
		print("DEBUG: txt read while waiting for Username: " + command)
	# once username is read, check each username to make sure it doesn't exist
	new_username = command
	user_found = None
	for x in users: 
		if (x.username == command):
			user_found = x
			break
	# end if no match is found
	# open file to write Not Found
	if (user_found != None):
		print("DEBUG: existing username found")
		with open("pipe_profiles.txt", "w") as pipe: 
			pipe.write("--existing_user_found--")
			pipe.flush()
		return
	# clear file and request Password
	print("DEBUG: no existing username found")
	with open("pipe_profiles.txt", "w") as pipe:
		pipe.write("--create_password--")
		pipe.flush()
	# open file to read Password
	command = "--create_password--" 
	while (command == "--create_password--"):
		time.sleep(2)
		with open("pipe_profiles.txt", "r") as pipe: 
			command = pipe.readline().strip()
		print("DEBUG: txt read while waiting for Password: " + command)
	# save new user to array
	new_password = command
	new_user = User(new_username, new_password)
	users.append(new_user)
	# check if last item in array is new user
	arr_len = len(users)
	if (new_username == users[arr_len-1].username):
		with open("pipe_profiles.txt", "w") as pipe:
			pipe.write("--success_create--")
			pipe.flush()
	else:
		with open("pipe_profiles.txt", "w") as pipe:
			pipe.write("--failed_create--")
			pipe.flush()
	return


def main():
	# open pipe file and clear it
	with open("pipe_profiles.txt", "w") as pipe: 
		pipe.write("")
		pipe.flush()

	# u1 = User("GHop95", "Beavers2001")
	# u2 = User("ObiWan", "MasterJedi")
	# u3 = User("hacker_man", "123456")
	# users = [u1, u2, u3]

	# populate array
	print("Populating array from users_saved.txt...")
	users = []
	try:
		with open("users_saved.txt", "r") as saves:
			lines = saves.readlines()
			for i in range(0, len(lines), 2):  # read two lines at a time (username, password)
				username = lines[i].strip()
				if i + 1 < len(lines):  # ensure there is a corresponding password
					password = lines[i + 1].strip()
					users.append(User(username, password))					
	except FileNotFoundError:
		file = open("users_saved.txt", 'w')
		print('File created')
		file.close()


	# begin waiting for command
	action = -1
	while (action != "--0--"):
		### uncomment to display users array
		# for x in users:
		# 	print(x.username +", "+ x.password)
		# print("")

		time.sleep(2)
		# open file to read 1, 2, or 0
		with open("pipe_profiles.txt", "r") as pipe: 
			action = pipe.readline().strip()
		print("DEBUG: txt read in main(): " + action)
		if (action == "--1--"):
			print("DEBUG: calling login_user_p()")
			login_user_p(users) # You cant clear file after this function because the client program needs time to read it.
		elif (action == "--2--"):
			print("DEBUG: calling create_user_p()")
			create_user_p(users)
			pass
	print("Quitting profiles")

	# save array
	print("Saving array to users_saved.txt...")
	with open("users_saved.txt", "w") as saves:
		for i, user in enumerate(users):
			saves.write(user.username + "\n" + user.password)  # write username and password
			if i < len(users) - 1:  # avoid adding a newline at the end
				saves.write("\n")  # add a newline *only* if it's not the last user


if __name__ == '__main__':
	main()
