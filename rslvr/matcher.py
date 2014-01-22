import operator

class EntityMatcher():

	def match(self, *args, **kwargs):
		return self._eq(self.s1, self.s2)

	def _eq(self):
		pass