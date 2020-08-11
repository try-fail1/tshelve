tshelve
========

Description
------------

A near dupicate of the `shelve <https://docs.python.org/3/library/shelve.html#module-shelve>`_ module,
but with `threading <https://docs.python.org/3/library/threading.html>`_ used under the
hood to speed up execution time.

Purpose
--------

Regular `shelve <https://docs.python.org/3/library/shelve.html#module-shelve>`_ operations can be
notoriously slow. The ``tshelve`` module 
aims to provide a more efficient program,
that is still similar to the built-in. 

Installation
-------------

Installing ``tshelve`` should be done with `PIP <https://pypi.org/project/pip/>`_:

.. code-block:: sh

    $ pip install tshelve

Benefits
-------------

* A more meaningful `repr <https://docs.python.org/3/library/functions.html#repr>`_:
    ``shelve``: ``'<shelve.Shelf object at 0x00572CB8>'``
    ``tshelve.TShelf``: ``TShelf(dict={}, protocol=5, writeback=False, keyencoding='utf-8')``

* Similar to the shelve module in the standard library.

The amount of speed up that ``tshelve``
brings will depend on the code. However,
there will usually be a speed-up, especially
in code that interacts heavily with the module.

The following block of code was run with
`shelve.open <https://docs.python.org/3/library/shelve.html#shelve.open>`_ and ``tshelve.open``.
Both ``tshelve`` and `shelve <https://docs.python.org/3/library/shelve.html#module-shelve>`_ were tested in
the same environment to ensure realistic results.

.. code-block:: python
    
    import shelve
    import tshelve

    sync_open = shelve.open('shell', writeback=True)
    thread_open = tshelve.open('shell', writeback=True)
    
    def speedup(opened):
        opened['testvalue'] = False
        opened['tester'] = 5324
        opened['tester']
        opened.get('testvalue')
        opened['testit'] = 'Hello'
        opened.items()
        opened.keys()
        opened.values()
        del opened['testit']
        'testvalue' in opened
        for _ in opened:
            pass
        opened.popitem()
        opened.sync()
        opened.close()
    
    speedup(sync_open)
    speedup(thread_open)

The difference in execution time between
the two is drastic. ``tshelve`` operations
were, on average, nearly 44% faster than those
found in the  `shelve <https://docs.python.org/3/library/shelve.html#module-shelve>`_ module.

Example
--------------

.. code-block:: python

    import tshelve

    with tshelve.open('shell') as f:
        f['fruit'] = ['apple', 'banana']
        f['language'] = 'Python'
        del f['fruit']
        print(f['language'])

License
---------

This module is currently licensed under the `MIT <https://en.wikipedia.org/wiki/MIT_License>`_ license.