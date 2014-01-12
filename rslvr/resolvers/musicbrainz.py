from resolvers import BaseResolver

class MusicBrainzResolver(BaseResolver):
	
	__name__ = 'musicbrainz'

	# endpoint
	http_method = 'get'
	base_url = 'http://musicbrainz.org/ws/2/recording/?fmt=json'
	search_url = ''
	search_param_key = 'query'

	# data mapping
	json_root_key = 'recording'
	field_map = [
        ('id',    	 		('id',)),
        #('album',    		('album', 'title')),
        ('artist',   		('artist-credit', 0, 'artist', 'name')),
        ('artist_id', 	('artist-credit', 0, 'artist', 'id')),
        ('duration', 		('duration',)),
        ('link',     		('link',)),
        ('name',    		('title',)),
    ]