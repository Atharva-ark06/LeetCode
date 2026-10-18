class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, text: str):
        node = self
        for char in text:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
