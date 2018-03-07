import hashlib
import uuid

def password_hash(password):
	password = password
	salt = uuid.uuid4().hex
	hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
	print (hashed_password)
	return hashed_password

password_hash("mwalugha")