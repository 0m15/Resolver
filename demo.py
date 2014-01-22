from rslvr.resolvers.deezer import DeezerResolver
from rslvr.resolvers.spotify import SpotifyResolver
from rslvr.resolvers.rdio import RdioResolver
from rslvr.resolvers.lastfm import LastfmResolver
from rslvr.resolvers.musicbrainz import MusicBrainzResolver
from rslvr.resolvers.nokiamusic import NokiaMusicResolver

from rslvr.resolver import ResolverService

resolvers = [
	# DeezerResolver,
	# SpotifyResolver,
	# LastfmResolver,
	NokiaMusicResolver
]

mr = ResolverService(resolvers)

tracks = [
	('how i could just kill a man', 'cypress hill'),
	('cypress hill how i could just kill a man', 'cypress hill', 'how i could just kill a man'),
	('harmony dumbo gets mad', 'dumbo gets mad', 'harmony'),
	('depeche mode enjoy the silence', 'depeche mode', 'enjoy the silence'),
	('the end summer camp', 'summer camp', 'the end'),
	('justice stress', 'justice', 'stress'),
	('1901 phoenix', 'phoenix', '1901'),
]

for i, t in enumerate(tracks):
	r = mr.resolve(t[0], fields=['id', 'name', 'artist', 'artist_id'], meta={})
	#r = mr.resolve(t[0], fields=['id', 'name', 'artist', 'artist_id'])
	
	print r.json(sort_keys=True, indent=4)

	print '\n'
	print '==============================='
	print '\n'