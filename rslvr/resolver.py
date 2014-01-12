import json

from multiprocessing import Process, Queue


class ResolverService():
	"""
	The main Resolver service.
	It support as many resolvers as you pass in the 

	    __init__(self, resolvers):
	
	function:

			r = ResolverService([DeezerResolver, ])
	
	An example resolvers dict is like this:

			resolvers = [
				'spotify': SpotifyResolver
				'rdio': RdioResolver
			]

	You can register at runtime a new resolver,
	by invoking the:

			register_resolver('name', ResolverClass):

	function, i.e.:

			register_resolver('rdio', RdioResolver)

	by doing that, further requests will also try to match
	the given query on that resolver as well.
	"""
	_resolvers = []

	def __init__(self, resolvers):
		for r in resolvers:
			self._resolvers.append(r())

	def register_resolver(self, resolver):
		self._resolvers.append(resolver())

	@property
	def results(self):
		return self.__results

	def json(self, **kwargs):
		return json.dumps(self.results, **kwargs)

	def resolve(self, *args, **kwargs):
		q = Queue()
		processes = []

		for resolver in self._resolvers:			
			p = Process(target=resolver.resolve, args=(args[0], q), kwargs=kwargs)
			p.start()
			processes.append(p)

		self.__results = [q.get() for p in processes]
		
		return self