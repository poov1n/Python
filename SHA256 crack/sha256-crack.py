# Test it in a test site to make the script errorfree

from pwn import *
import sys

#to get parameters to be input in cmd line, we use sys.arg
if len(sys.argv) != 2: # we expect 1 parameter, the first parameter would be the name of the file
	print("invalid argumets")
	print(">>{} <sha256sum>".format(sys.argv[0])) # telling the user that the input function must be of a SHA value
	exit()

wanted_hash = sys.argv[1]
password_file ="ssh-common-passwords.txt" #location of the file to match the crack, could use rockyou.txt 
attempts = 0

#we are using the log.process which get imported with the pwn module

with log.progress("Attempting to crack: {}!\n".format(wanted_hash)) as p:
	with open(password_file,"r", encoding="latin-1") as password_list:
		for password in password_list:
			password = password.strip("\n").encode("latin-1")
			password_hash = sha256sumhex(password) #sha256 is another function that gets imported from pwn module
			p.status("[{}] {} == {}".format(attempts,password.decode("latin-1"), password_hash)) #using pwn modules log function to see attempts
			if password_hash == wanted_hash:
				p.success("Password has found after {} attempts! {} hashes to {}!".format(attempts,password.decode("latin-1"),password_hash)) 
				exit()
			attempts += 1
		p.failure ("Password hash not found!")

