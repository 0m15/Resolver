from rslvr.resolvers.deezer import DeezerResolver
from rslvr.resolvers.spotify import SpotifyResolver
from rslvr.resolvers.rdio import RdioResolver
from rslvr.resolvers.lastfm import LastfmResolver
from rslvr.resolvers.musicbrainz import MusicBrainzResolver

from rslvr.resolver import ResolverService

resolvers = [
	DeezerResolver,
	SpotifyResolver,
  # RdioResolver,
	LastfmResolver,
	# MusicBrainzResolver
]

mr = ResolverService(resolvers)

tracks = [
	('Bocuma', 'Boards of canada'),
]

for t in tracks:
	r = mr.resolve(t[0], fields=['id', 'name', 'artist', 'artist_id'], meta={'artist': t[1]})
	#r = mr.resolve(t, fields=['id', 'name', 'artist'])
	print r.json(sort_keys=True, indent=4)
	print '\n'
	print '==============================='
	print '\n'