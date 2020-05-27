import unittest

from src.hash_table import ChainHashTable


class TestChainHashTable(unittest.TestCase):
    def test_insert(self):
        ht = ChainHashTable(8)
        self.assertTrue(ht.insert("3", "a"))
        self.assertTrue(ht.insert("3", "b"))
        self.assertTrue(ht.insert("11", "c"))

    def test_remove(self):
        ht = ChainHashTable(8)
        ht.insert("3", "a")
        self.assertTrue(ht.remove("3"))
        ht.insert("4", "b")
        ht.insert("5", "c")
        self.assertTrue(ht.remove("4"))
        ht.insert("6", "d")
        self.assertTrue(ht.remove("5"))
        self.assertTrue(ht.remove("6"))
        self.assertFalse(ht.remove("8"))

    def test_search(self):
        ht = ChainHashTable(8)
        ht.insert("3", "a")
        self.assertEqual(ht.search("3"), "a")
        ht.insert("3", "b")
        self.assertEqual(ht.search("3"), "b")
        ht.insert("11", "c")
        self.assertEqual(ht.search("11"), "c")

    def test_all(self):
        pass


if __name__ == "__main__":
    unittest.main()
