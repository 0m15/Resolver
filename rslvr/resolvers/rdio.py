from resolvers import BaseResolver
import requests
from requests_oauthlib import OAuth2
from requests.auth import HTTPBasicAuth


class RdioResolver(BaseResolver):
	"""
	Based on the oAuth2 protocol.
	"""

	__name__ = 'rdio'

	# endpoint
	http_method = 'post'
	base_url = 'https://www.rdio.com/api/1/'
	search_url = 'search'
	token_url = 'https://www.rdio.com/oauth2/token'

	# oauth
	oauth2 = {
		'client_id': 'RIcB7TTvsUpFe7WfrJN0uQ',
		'client_secret': 'EXK_ZKu58arGedOBftLmeg',
	}
	token = None

	# results
	search_param_key = 'query'
	json_root_key = 'result'

	field_map = [
        ('id',    	 		('key',)),
        ('album',				('album',)),
        ('artist',			('artist',)),
        ('artist_id',		('artistKey',)),
        ('name',				('name',))
    ]

	def __init__(self):
		if not self.token:
			payload = {'grant_type': 'client_credentials'}
			self._token_request(payload)

	def _set_token(self, token):
		"Save the access token for future requests"
		self.token = token

	def _token_request(self, payload):
		"Obtain a fresh access token"
		r = requests.post(self.token_url, 
						auth=HTTPBasicAuth(self.oauth2['client_id'], self.oauth2['client_secret']),
            data=payload)
		self._set_token(r.json())

	def _make_request(self, url, query):
		"""
		We need to override the `_make_request` method as well,
		to properly sign api request with our access token.
		"""
		payload = {'method': self.search_url, 'types': 'track', self.search_param_key: query}
		oauth = OAuth2(token=self.token)
		return getattr(requests, self.http_method)(url, auth=oauth, data=payload)

	def _parse(self, resp):
		return resp.json()[self.json_root_key]['results'][0]