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
	MusicBrainzResolver
]

mr = ResolverService(resolvers)

tracks = ['Autumn Leaves']

for t in tracks:
	r = mr.resolve(t, fields=['id', 'name', 'artist'], meta={'artist':'Roger Williams'})
	print r.json(sort_keys=True, indent=4)