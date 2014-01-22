from . import BaseResolver

class LastfmResolver(BaseResolver):
	
	__name__ = 'lastfm'

	# endpoint
	http_method = 'get'
	base_url = 'http://ws.audioscrobbler.com/2.0/'
	search_url = '?method=track.search&api_key=3bbf4555e4b9157cef8474458b592d66&format=json'
	search_param_key = 'track'

	# data map
	json_root_key = 'results'

	field_map = [
	    ('id',    	 		('mbid',)),
	    ('artist',   		('artist',)),
	    ('link',     		('url',)),
	    ('name',    		('name',)),
	    ('listeners',   	('listemers',))
  	]

	def _parse(self, resp):
		r = resp.json()[self.json_root_key]['trackmatches']['track']
		if isinstance(r, dict):
			return [r]
		return r

	def _is_valid_response(self, resp):
		data = resp.json()
		root_key = self.json_root_key
		return (resp.status_code == 200 and root_key in data and 'track' in data[root_key]['trackmatches'])