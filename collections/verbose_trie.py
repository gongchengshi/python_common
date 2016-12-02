class VerboseTrieNode:
    def __init__(self, parent=None, key=None):
        self.value = None
        self.children = {}
        self.parent = parent
        self.key = key

    def add_child(self, key):
        if key in self.children:
            child = self.children[key]
        else:
            child = VerboseTrieNode(self, key)
            self.children[key] = child

        return child

    def get_child(self, key):
        return self.children.get(key, None)


class VerboseTrie:
    def __init__(self):
        self.root = VerboseTrieNode()

    def add_keys(self, keys):
        node = self.root
        for key in keys:
            node = node.add_child(key)
        node.value = keys

    def find_matches(self, input):
        pass

    def to_list(self):
        """Do an iterative pre-order traversal to get."""
        node_stack = [(k, n) for k, n in self.root.children.iteritems()]
        contents = []

        while node_stack:
            key, node = node_stack.pop()

            if node.children:
                node_stack += [(k, n) for k, n in node.children.iteritems()]
            else:
                l = []
                while node and node.key:
                    l.append(node.key)
                    node = node.parent
                contents.append(reversed(l))
        return contents


def recursive_preorder_traversal(node, action, l):
    if not node.children:
        action(l)
    else:
        for word, child in node.children.iteritems():
            recursive_preorder_traversal(child, action, l + [word])
