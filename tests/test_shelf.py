import unittest
import tshelve

class Tester(unittest.TestCase):
    
    def setUp(self):
        self.maxDiff = None
        self.internal = tshelve.TShelf({})

    def test_bytes(self):
        self.internal['testkey'] = 123
        for i in self.internal.dict.popitem():
            self.assertIsInstance(i, bytes)

    def test_ctx_mnger(self):
        with self.internal as f:
            self.assertIsInstance(f, tshelve.TShelf)

unittest.main()
