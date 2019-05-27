class ObjectShare:
    _share = {}

    def __init__(self, objectInit):
        self.objectInit = objectInit

    def get(self, *args, **kwargs):
        key = args, frozenset(kwargs.items())
        if key not in self._share:
            self._share[key] = self.objectInit(*args, **kwargs)
        return self._share[key]