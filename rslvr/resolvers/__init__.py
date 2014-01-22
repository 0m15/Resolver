# -*- coding: utf-8 -*-
import operator
import requests
import json

from requests_oauthlib import OAuth2Session, OAuth1Session

class BaseResolver():
	"""
	A base Resolver class, every resolver must inherits from
	this class and should implements all required methods as well.
	
	Data strucure mapping
	---------------------

	Here's an example of mapping a specific provider object
	to a consistent data strucure. 

	Given the following json item:

		 	{
				'id': 123,
				'artist': {'name': 'Zebda', 'id': 456},
				'track': {'title': 'Motivés', 'album': 'Motivés'}
			}
	
	`field_map` attribute will be defined as follow:

			field_map = [
				('id', 		 (		'id')), 						 # data['id']
				('artist', (		'artist', 'name')),  # data['artist']['name']
				('name', 	 (		'track',  'title')), # data['track']['title']
			]

	that will generate the following results:

			{
				'id': 123,
				'artist': 'Zebda',
				'name': 'Motivés'
			}

	"""

	__name__ = ''

	# http api
	http_method = 'get'
	oauth2 = False

	# endpoints
	base_url = ''
	search_url = ''
	search_param_key = ''

	# default fields to return (see field_map)
	default_fields = ['id',]
	
	# json root object
	json_root_key = ''
	
	# example field map
	field_map = [
		('id', 		 ('id')),	
		('artist',   ('artist', 'name')),
	]

  	# - end of attributes to override -

  	__results = {}
  	
	def resolve(self, *args, **kwargs):
		return self._search(*args, **kwargs)

	def to_json(self):
		return json.dumps(self.__results, sort_keys=True)

	def _search(self, *args, **kwargs):

		self.default_fields = kwargs.get('fields', self.default_fields)
		meta = kwargs.get('meta', {})

		url = self.base_url + self.search_url
		query = args[0]
		queue = args[1] # process queue

		resp = self._make_request(url, query)
		if not self._is_valid_response(resp):
			return queue.put({ self.__name__: None })
		
		entity = self._match_entity(self._parse(resp), meta)
		return queue.put(self._results(entity))

	def _make_request(self, url, query):
		payload = { self.search_param_key: query }
		if self.http_method == 'get':
			return requests.get(url, params=payload)
		return requests.post(url, data=payload)

	def _parse(self, resp):
		print 'resp'
		return resp.json()[self.json_root_key]

	def _is_valid_response(self, resp):

		root_key = self.json_root_key
		return (resp.status_code == 200 
	    				and root_key in resp.json()
	    				and len(resp.json()[root_key]) > 0)

	def _match_entity(self, data, meta):
		entities = []
		matched_parts = []

		for item in data:
			entities.append(self._map_item(item))

		for entity in entities:
			if not meta:
				return entity

			for key in meta:
				if self._eq(meta[key], entity[key]):
					matched_parts.append(key)

			if len(matched_parts) == len(meta.items()):
				return entity
			else:
				matched_parts = []

	def _eq(self, a, b):
		"""
		Equality function. Can be overriden with any algorithm
		you want, it accepts two strings to compare, `s1` and `s2`
		and should return a `Boolean` based on the string comparison
		results. 
		"""
		treshold = 0.9
		a = a.lower()
		b = b.lower()
		if not len(a) or not len(b): 
			return 0.0
		if len(a) == 1:  a=a+u'.'
		if len(b) == 1:  b=b+u'.'

		a_bigram_list=[]
		for i in range(len(a)-1):
			a_bigram_list.append(a[i:i+2])
		b_bigram_list=[]
		for i in range(len(b)-1):
			b_bigram_list.append(b[i:i+2])
	 
		a_bigrams = set(a_bigram_list)
		b_bigrams = set(b_bigram_list)
		overlap = len(a_bigrams & b_bigrams)
		dice_coeff = overlap * 2.0/(len(a_bigrams) + len(b_bigrams))
	    
		return dice_coeff > treshold
		

	def _map_item(self, data):
		mapped = {}
		for field in self.field_map:
			k = field[0]
			if not k in self.default_fields:
				continue
			try:
				mapped[k] = reduce(operator.getitem, field[1], data)
			except KeyError:
				pass
		return mapped

	def _results(self, data):
		self.__results[self.__name__] = data
		return self.__results