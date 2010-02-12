class Cache(object):

    def __init__(self, backend, namespace=None):
        if namespace:
            self.namespace = namespace
        self.backend = backend

    def get_key(self, key):
        if hasattr(self, 'namespace'):
            return "%s:%s" % (self.namespace, key)
        return key

    def cache(self, key, callable_, expire=0):
        try:
            k = self.get_key(key)
            v = self.backend.get(k)
            return v
        except KeyError:
            value = callable_()
            self.backend.set(self.get_key(key), value, expire=expire)
            return value

    def clear(self):
        self.backend.clear()
