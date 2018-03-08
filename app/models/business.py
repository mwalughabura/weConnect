businesses = {}

class Business():

	def __init__(self):
		self.thisBusiness = {}


	def register_business(self, name, location, biz_type, description):
		if name not in businesses:
			self.thisBusiness['business_name'] = name
			self.thisBusiness['location'] = location
			self.thisBusiness['business_type'] =  biz_type
			self.thisBusiness['description'] = description
			itemno = len(businesses)
			bizno = str(itemno + 1)
			businesses[bizno] = self.thisBusiness
			return "Business has been successfully created."
		return "The name has already been taken."