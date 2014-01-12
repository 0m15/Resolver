import operator

class EntityMatcher():
	
	def __init__(self, s1, s2, treshold=0.95):
		self.s1 = s1
		self.s2 = s2
		self.treshold = treshold

	def match(self, *args, **kwargs):
		return self._distance(self.s1, self.s2)

	def _distance(self):
		pass