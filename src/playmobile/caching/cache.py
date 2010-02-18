from playmobile.caching.backend import NoCacheBackend

class Cache(object):

    default_options = {'expire': 0,
        'namespace': None}

    def __init__(self, backend=None, **kw):
        self.options = self.default_options.copy()
        self.options.update(kw)
        if backend is None:
            backend = NoCacheBackend()
        self.backend = backend

    def get_key(self, key):
        if self.options.has_key('namespace'):
            return "%s:%s" % (self.options['namespace'], key)
        return key

    def cache(self, key, callable_, expire=None):
        try:
            k = self.get_key(key)
            v = self.backend.get(k)
            return v
        except KeyError:
            value = callable_()
            self.backend.set(self.get_key(key), value,
                expire=expire or self.options['expire'])
            return value

    def clear(self):
        self.backend.clear()


