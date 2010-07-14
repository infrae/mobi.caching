from mobi.caching.backend import NoCacheBackend

class Cache(object):

    default_options = {'expires': 0,
        'namespace': None}

    def __init__(self, backend=None, **kw):
        self.options = self.default_options.copy()
        self.options.update(kw)
        if backend is None:
            backend = NoCacheBackend()
        self.backend = backend

    def cache(self, key, callable_, expires=None):
        try:
            k = self.__get_key(key)
            v = self.backend.get(k)
            return v
        except KeyError:
            value = callable_()
            self.backend.set(self.__get_key(key), value,
                expires=(expires or self.options['expires']))
            return value

    def clear(self):
        self.backend.clear()

    def __get_key(self, key):
        namespace = self.options.get('namespace')
        if namespace is not None:
            return "%s:%s" % (self.options.get('namespace'), key)
        return key


