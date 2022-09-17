class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self,k):
        self.v = 0
        self.k = k
        self.children = {}
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode(None)

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode(w)
            node = node.children[w]
        node.v += 1
        
    def _startsWith(self,prefix):
        """
        @param {string} prefix
        @return {TrieNode} or None
        """
        node = self.root
        for w in prefix:
            if w in node.children:
                node = node.children[w]
            else:
                return None
        return node
        
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self._startsWith(word)
        if node and node.v:
            return True
        else:
            return False
        
    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        if self._startsWith(prefix):
            return True
        else:
            return False
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)