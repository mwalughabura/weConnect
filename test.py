dic = {'mwalugha': ['mwalughabura@gmail.com', 'password'], 'hamisi': ['hamisibura@gmail.com', 'password']}
lis = ['mwalughabura@gmail.com', 'password']

def email_in_db(email):
	for i in dic:
		if email in dic[i]:
			return "Hey"
	return "Ooops"

print(email_in_db('mwalughabura@gmail.com'))
print ("on to the next one.")
print(email_in_db('hamisibura@gmail.com'))