from .thread import get_in_thread


def meth(name):
    def inner(self, *args, **kwargs):
        return get_in_thread((getattr(self._hide, name), args, kwargs))
    return inner


def add_to_class(shelf_stuff):
    def classy(cls):
        for i in shelf_stuff:
            setattr(cls, i, meth(i))
        return cls
    return classy
