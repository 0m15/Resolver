from resolvers.deezer import DeezerResolver
from resolvers.spotify import SpotifyResolver
from resolvers.rdio import RdioResolver
from resolvers.lastfm import LastfmResolver
from resolvers.musicbrainz import MusicBrainzResolver

from resolver import ResolverService

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