class TrieNode:
    def __init__(self):
        self.value = None
        self.children = {}

    def add_child(self, key):
        if key in self.children:
            child = self.children[key]
        else:
            child = TrieNode()
            self.children[key] = child

        return child

    def get_child(self, key):
        return self.children.get(key, None)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_keys(self, keys):
        node = self.root
        for key in keys:
            node = node.add_child(key)
        node.value = keys

    def find_matches(self, input):
        pass
