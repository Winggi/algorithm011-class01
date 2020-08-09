class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node.keys():
                node[c] = dict()
                node = node[c]
            else:
                node = node[c]
        node['EOS'] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node.keys():
                return False
            else:
                node = node[c]
        if 'EOS' in node.keys():
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node.keys():
                return False
            else:
                node = node[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)