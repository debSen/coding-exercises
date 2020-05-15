class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def _char_to_int(self, char):
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tcrawl = self.root
        for level in range(len(word)):
            index = self._char_to_int(word[level])
            if not tcrawl.children[index]:
                tcrawl.children[index] = TrieNode()
            tcrawl = tcrawl.children[index]
        tcrawl.endOfWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tcrawl = self.root
        for level in range(len(word)):
            index = self._char_to_int(word[level])
            if not tcrawl.children[index]:
                return False
            tcrawl = tcrawl.children[index]
        return tcrawl != None and tcrawl.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tcrawl = self.root
        for level in range(len(prefix)):
            index = self._char_to_int(prefix[level])
            if not tcrawl.children[index]:
                return False
            tcrawl = tcrawl.children[index]
        return True

# Test Code
def stub():
    pass
    
