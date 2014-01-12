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
		('artist', ('artist', 'name')),
	]

	__results = {}
  
  # - end of attributes to override -

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
			return {}
		
		entity = self._match_entity(self._parse(resp), meta)
		return queue.put(self._results(entity))

	def _make_request(self, url, query):
		payload = { self.search_param_key: query }
		if self.http_method == 'get':
			return requests.get(url, params=payload)
		return requests.post(url, data=payload)

	def _parse(self, resp):
		return resp.json()[self.json_root_key]

	def _match_entity(self, data, meta):
		entities = []
		for item in data:
			entities.append(self._map_item(item))
		
		for entity in entities:
			if not meta:
				return entity
			for key in meta:
				if entity[key].lower() == meta[key].lower(): 
					return entity
		return None

	def _is_valid_response(self, resp):
		root_key = self.json_root_key
		return (resp.status_code == 200 
	    				and root_key in resp.json()
	    				and len(resp.json()[root_key]) > 0)

	def _map_item(self, data):
		mapped = {}
		for field in self.field_map:
			k = field[0]
			if not k in self.default_fields:
				continue
			mapped[k] = reduce(operator.getitem, field[1], data)
		return mapped

	def _results(self, data):
		self.__results[self.__name__] = data
		return self.__results