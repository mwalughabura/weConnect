import hashlib, uuid
import re


users = {}

class User():
	logs = []

	def __init__(self):
		pass

	def password_hash(self, password):
		self.password = password
		salt = uuid.uuid4().hex
		hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
		return hashed_password

	def check_username_or_email(self, user_input):
		match = re.search(r'[\w.-]+@[\w.-]+.\w+', user_input)

		if match:
			return "It is a valid email."
		return "It is a username."

	def username_in_db(self, username):
		if username in users:
			return "Hey"
		return "Ooops"

	def email_in_db(self, email):
		for i in users:
			if email in users[i]:
				return "Hey"
		return "Ooops"

	def create_user(self, username, email, password, confirm_password):
		if username not in users:
			if password == confirm_password:
				passwordHashed = self.password_hash(password)
				users[username] = [email, password, passwordHashed]
		return "User has been successfully created."

	def user_login(self, username_or_email, password):
		checkEmailorName = self.check_username_or_email(username_or_email)
		if checkEmailorName == "It is a username.":
			in_db = self.username_in_db(username_or_email)
			if in_db == "Hey":
				if users[username_or_email][1] == password:
					return "Successfully logged in."
			return "Check your fields."
		elif checkEmailorName == "It is a valid email.": 
			in_db = self.email_in_db(username_or_email)
			if in_db == "Hey":
				for i in user:
					if email in users[i]:
						if users[i][1] == password:
							return "Successfully logged in."
			return "Check your fields."
		return "Check your fields."

