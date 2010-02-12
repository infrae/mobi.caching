_marker = object()

class NoCacheBackend(object):

    def get(self, key):
        raise KeyError, 'no cache'

    def set(self, key, value, **options):
        pass

    def clear(self, key):
        pass

class DictBackend(object):
    """ The GIL makes it thread safe
    but some other implementations may not be thread safe
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

    def clear(self, key):
        return self.dictionary.clear()
