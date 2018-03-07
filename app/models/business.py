businesses = {}

class Business():

	# def __init__(self):
	# 	pass


	def __init__(self, name, location, biz_type, description):
		if name not in businesses:
			businesses[name] = [location, biz_type, description]
		return "Business has been successfully created."

biz = Business('Mwalugha', 'Nairobi', 'LTD', 'The best business in Kenya.')
print (businesses)