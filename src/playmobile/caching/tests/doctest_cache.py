"""
    >>> from playmobile.caching import Cache
    >>> from playmobile.caching.backend import NoCacheBackend, DictBackend

    We instantiate a cache engine.

    >>> cache_engine = Cache(namespace='somename')

    By default cache backend is no cache.

    >>> cache_engine.backend #doctest: +ELLIPSIS
    <playmobile.caching.backend.NoCacheBackend object at ...>

    >>> cache = cache_engine.cache

    the cache method call the provided callable and cache it. But if the engine
    is NoCacheBackend, nothing gets cached.

    >>> cache('somekey', get_a)
    a called
    'a'
    >>> cache('somekey', get_a)
    a called
    'a'

    If we change the backend to a real cache backend. The callable is cached

    >>> cache_engine.backend = DictBackend()
    >>> cache('somekey', get_a)
    a called
    'a'
    >>> cache('somekey', get_a)
    'a'
    >>> cache('somekey', get_b)
    'a'
    >>> cache('b key', get_b)
    b called
    'b'

    The cache can be cleared.

    >>> cache_engine.clear()
    >>> cache('somekey', get_a)
    a called
    'a'

"""

def get_a():
    print "a called"
    return "a"

def get_b():
    print "b called"
    return "b"
