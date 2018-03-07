businesses = {}

class Business():

	def __init__(self):
		pass


	def register_business(self, name, location, biz_type, description):
		if name not in businesses:
			businesses[name] = [location, biz_type, description]
		return "Business has been successfully created."
