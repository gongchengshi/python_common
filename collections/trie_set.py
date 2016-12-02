class TrieSetNode:
    def __init__(self):
        self.value = False
        self.children = {}

    def add_child(self, key):
        if key in self.children:
            child = self.children[key]
        else:
            child = TrieSetNode()
            self.children[key] = child

        return child

    def get_child(self, key):
        return self.children.get(key, None)


class TrieSet:
    def __init__(self):
        self.root = TrieSetNode()

    def add(self, key):
        node = self.root
        for item in key:
            node = node.add_child(item)
        node.value = True

    def __contains__(self, key):
        node = self.root
        for item in key:
            node = node.get_child(item)
            if node is None:
                return False

        return node.value
