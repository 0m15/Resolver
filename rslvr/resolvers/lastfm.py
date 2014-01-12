from resolvers import BaseResolver

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
    ('listeners',   ('listemers',))
  ]

	def _parse(self, resp):
		return resp.json()[self.json_root_key]['trackmatches']['track']