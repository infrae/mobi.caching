# init

from playmobile.caching.cache import *
from playmobile.caching.backend import NoCacheBackend

default_cache = Cache(NoCacheBackend(), 'default')
cache = default_cache.cache
clear = default_cache.clear
