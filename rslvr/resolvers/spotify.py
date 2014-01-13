from . import BaseResolver
 
class SpotifyResolver(BaseResolver):

	__name__ = 'spotify'

	# endpoint
	method = 'get'
	base_url = 'http://ws.spotify.com/search/1/'
	search_url = 'track.json'
	search_param_key = 'q'

	# data mapping
	json_root_key = 'tracks'
	field_map = [
        ('id',    	 		('href',)),
        ('album',    		('album', 'name')),
        ('artist',   		('artists', 0, 'name')),
        ('artist_id',   ('artists', 0, 'href')),
        ('name',    		('name',)),
    ]