from repoze.lru import LRUCache

_marker = object()


class NoCacheBackend(object):

    def get(self, key):
        raise KeyError, 'no cache'

    def set(self, key, value, **options):
        return value

    def clear(self):
        pass


class DictBackend(object):
    """ The GIL makes it thread safe
    """

    def __init__(self):
        self.dictionary = {}

    def get(self, key):
        value = self.dictionary.get(key, _marker)
        if value is _marker:
            raise KeyError, 'no cache value for key: %s' % key
        return value

    def set(self, key, value, **options):
        self.dictionary[key] = value

    def clear(self):
        return self.dictionary.clear()


class LRUBackend(LRUCache):

    def get(self, key):
        val = super(LRUBackend, self).get(key, _marker)
        if val is _marker:
            raise KeyError
        return val

    def set(self, key, value, **options):
        return self.put(key, value)


names = {
    'no-cache': NoCacheBackend,
    'dict': DictBackend,
    'lru': LRUBackend,
    # 'memcache': ...
}
