from . import BaseResolver

class NokiaMusicResolver(BaseResolver):
	
	__name__ = 'nokiamusic'

	# endpoint
	http_method = 'get'
	base_url = 'http://api.mixrad.io/1.x/it/?domain=music&client_id=e9e04166dbdb93ac34206ebbf3206ff1&category=track&itemsperpage=100'
	##http://api.mixrad.io/1.x/it/?domain=music&q=justice%20stress&client_id=e9e04166dbdb93ac34206ebbf3206ff1
	search_url = ''
	search_param_key = 'q'

	# data mapping
	json_root_key = 'items'

	field_map = [
        ('id',    	 		('id',)),
        #('album',    		('album', 'title')),
        ('artist',   		('creators', 'performers', 0, 'name',)),
        ('artist_id',  		('creators', 'performers', 0, 'id',)),
        # ('duration', 		('duration',)),
        # ('link',     		('link',)),
        ('name',    		('name',)),
    ]

	def _parse(self, resp):
		print resp.url
		return resp.json()[self.json_root_key]
