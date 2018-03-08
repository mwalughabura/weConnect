# from werkzeug.security import generate_password_hash, check_password_hash
import hashlib, uuid


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

	def create_user(self, username, email, password, confirm_password):
		if username not in users:
			if password == confirm_password:
				password = self.password_hash(password)
				users[username] = [email, password]
		return "User has been successfully created."

	def user_login(self):
		pass