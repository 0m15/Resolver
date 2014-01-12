from resolvers import BaseResolver

class DeezerResolver(BaseResolver):
	
	__name__ = 'deezer'

	# endpoint
	http_method = 'get'
	base_url = 'http://api.deezer.com/2.0/'
	search_url = 'search'
	search_param_key = 'q'

	# data mapping
	json_root_key = 'data'
	field_map = [
        ('id',    	 		('id',)),
        ('album',    		('album', 'title')),
        ('artist',   		('artist', 'name')),
        ('artist_id',   ('artist', 'id')),
        ('duration', 		('duration',)),
        ('link',     		('link',)),
        ('name',    		('title',)),
    ]