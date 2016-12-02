import unittest

from python_common.collections.trie_set import TrieSet


class TestTrieSet(unittest.TestCase):
    def test_trie_set(self):
        target = TrieSet()

        target.add('abcd')
        target.add('abc')
        target.add('aaa')
        target.add('bca')
        self.assertIn('abc', target)
        self.assertIn('abcd', target)
        self.assertIn('aaa', target)
        self.assertIn('bca', target)
        self.assertNotIn('dfg', target)
        self.assertNotIn('d', target)
