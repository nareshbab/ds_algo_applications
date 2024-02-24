
## ---------- TRIES --------------##

class TrieNode:

    def __init__(self) -> None:
        self.children = [None for _ in range(26)]

        # is_eow: is end of word is True if it
        # represents the end of word

        self.is_eow = False

class Trie:

    def __init__(self) -> None:
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()
    
    def _charToIndex(self, ch):
        return ord(ch) - ord('a')
    
    def insert(self, key):
        """
        If not present, insert into trie
        if the key is prefix of trie node,
        just marks leaf node
        """
        root = self.root
        length = len(key)

        for level in range(length):
            # take index for each character
            idx = self._charToIndex(key[level])
            
            # if current character is not present
            if not root.children[idx]:
                root.children[idx] = self.getNode()
            
            root = root.children[idx]
        
        root.is_eow = True

    def search(self, key):

        root = self.root
        length = len(key)

        for level in range(length):
            idx = self._charToIndex(key[level])

            if not root.children[idx]:
                return False
            root = root.children[idx]

        return root.is_eow
    

if __name__ == '__main__':
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    output = ["Not present in trie", "present in trie"]

    # Create Trie object
    t = Trie()

    for key in keys:
        t.insert(key)

    # Search for different keys
        
    print("{} ------- {}".format("the", output[t.search("the")]))
    print("{} ------- {}".format("these", output[t.search("these")]))
    print("{} ------- {}".format("their", output[t.search("their")]))
    print("{} ------- {}".format("thaw", output[t.search("thaw")]))
    print("{} ------- {}".format("an", output[t.search("an")]))


