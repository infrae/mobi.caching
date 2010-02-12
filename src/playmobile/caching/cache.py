class Cache(object):

    def __init__(self, backend, prefix=None):
        if prefix:
            self.prefix = prefix
        self.backend = backend

    def get_key(self, key):
        if hasattr(self, 'prefix'):
            return "%s:%s" % (self.prefix, key)
        return key

    def cache(self, key, callable_, expire=0):
        """ cache the 
        """
        try:
            k = self.get_key(key)
            v = self.backend.get(k)
            print "cache hit %s" % k
            return v
        except KeyError:
            value = callable_()
            self.backend.set(self.get_key(key), value, expire=expire)
            return value

    def clear(self):
        self.backend.clear()

