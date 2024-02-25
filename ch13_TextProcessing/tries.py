
## ---------- TRIES --------------##

# Total nodes of trie =  count of unique prefixes

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
    
    def getRoot(self):
        return self.root
    
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
    
    def count_nodes(self, root) -> int:        
        count = 0
        for i in range(26):
            if root.children[i]:
                count += self.count_nodes(root.children[i])
        return count + 1
    
    def word_break(self, key):

        if len(key) == 0:
            return True
        
        for i in range(1,len(key)+1):
            first_part = key[0:i]
            second_part = key[i:len(key)]

            if self.search(first_part) and self.word_break(second_part):
                return True
        
        return False
    
"""
Substrings of a string have a unique property i.e
all substrings = all prefixes of all suffixes

for eg. lets say string = "ababa"
Suffixes -> Prefixes
    ababa -> a, ab, aba, abab, ababa
        baba -> b, ba, bab, baba
        aba -> a, ab, aba
        ba -> b, ba
        a -> a
        "" -> ""
"""
def count_unique_substrings(key):
    
    suffixes = []

    for i in range(len(key)):
        suffixes.append(key[i:])

    t = Trie()

    for suffix in suffixes:
        t.insert(suffix)

    root = t.getRoot()    
    return t.count_nodes(root)
    

"""
Longest word with all prefixes:
We know that nodes in trie represents all the prefixes
so we want to traverse a branch which is longest and all nodes are eow
"""
def longest_word_prefix(root, temp):
    global longest_word

    for i in range(26):
        if root.children[i] and root.children[i].is_eow:
            temp += chr(i + ord('a'))
            if len(temp) > len(longest_word):
                longest_word =  temp
            longest_word_prefix(root.children[i], temp)
            temp = temp[:-1]



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

    keys2 = ["i", "like", "sam", "samsung", "mobile"]
    t2 = Trie()
    for key in keys2:
        t2.insert(key)
    print(t2.word_break("ilikesamsung"))


    ## Counting unique substrings
    keys3 = "apple"

    print(count_unique_substrings(keys3))


    keys4 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

    t3 = Trie()

    for word in keys4:
        t3.insert(word)

    t3_root = t3.getRoot()
    longest_word = ""
    longest_word_prefix(t3_root, "")
    print(longest_word)