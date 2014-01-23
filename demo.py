from rslvr.resolvers.deezer import DeezerResolver
from rslvr.resolvers.spotify import SpotifyResolver
from rslvr.resolvers.musicbrainz import MusicBrainzResolver
from rslvr.resolvers.nokiamusic import NokiaMusicResolver

from rslvr.resolver import ResolverService

resolvers = [
	DeezerResolver,
	SpotifyResolver,
	NokiaMusicResolver
]

mr = ResolverService(resolvers)

tracks = [
	('cypress hill how i could just kill a man', 'cypress hill'),
	('1901 phoenix', 'phoenix'),
]

for i, t in enumerate(tracks):
	r = mr.resolve(t[0], fields=['id', 'name', 'artist', 'artist_id'], meta={})
	
	print r.json(sort_keys=True, indent=4)

	print '\n'
	print '==============================='
	print '\n'