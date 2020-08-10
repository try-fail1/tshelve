import shelve
import dataclasses
from pickle import HIGHEST_PROTOCOL

from .usefuls import add_to_class


base = [
        '__iter__',
        '__contains__',
        'get',
        '__getitem__',
        '__setitem__',
        '__delitem__',
        '__del__',
        'sync',
        'close',
        'clear',
        'items',
        'keys',
        'pop',
        'popitem',
        'setdefault',
        'update',
        'values'
    ]


@dataclasses.dataclass
@add_to_class(base)
class TShelf(shelve.Shelf):
    """A threaded version of :class:`shelve.Shelf`"""
    dict: dict
    protocol: int = HIGHEST_PROTOCOL
    writeback: bool = False
    keyencoding: str = 'utf-8'

    def __post_init__(self):
        self._hide = shelve.Shelf(
            self.dict, self.protocol,
            self.writeback, self.keyencoding
            )


@dataclasses.dataclass
@add_to_class(['first', 'previous', 'next', 'last', 'set_location'] + base)
class TBsDbShelf(shelve.Shelf):
    """A threaded version of :class:`shelve.BsDbShelf`"""
    dict: dict
    protocol: int = HIGHEST_PROTOCOL
    writeback: bool = False
    keyencoding: str = 'utf-8'

    def __post_init__(self):
        self._hide = shelve.BsdDbShelf(
            self.dict, self.protocol,
            self.writeback, self.keyencoding
            )


@dataclasses.dataclass
@add_to_class(base)
class TDbfilenameShelf(shelve.Shelf):
    """A threaded version of :class:`shelve.DbfilenameShelf`"""
    filename: str
    flag: str = 'c'
    protocol: int = HIGHEST_PROTOCOL
    writeback: bool = False

    def __post_init__(self):
        self._hide = shelve.DbfilenameShelf(
            self.filename, self.flag,
            self.protocol, self.writeback)


def open(filename, flag='c', protocol=None, writeback=False):
    return TDbfilenameShelf(filename, flag, protocol, writeback)
