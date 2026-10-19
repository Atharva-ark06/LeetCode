class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.terminal = True

    def search(self, word: str) -> bool:
        def visit(node, index):
            if index == len(word):
                return node.terminal
            char = word[index]
            if char == ".":
                return any(visit(child, index + 1) for child in node.children.values())
            return char in node.children and visit(node.children[char], index + 1)
        return visit(self.root, 0)
