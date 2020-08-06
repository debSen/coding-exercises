class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_of_word = True
        
    def dfs(self, node, word, i):
        if i == len(word): return node.end_of_word

        if word[i] == ".":
            for child in node.children:
                if self.dfs(node.children[child], word, i+1): return True

        if word[i] in node.children:
            return self.dfs(node.children[word[i]], word, i+1)

        return False
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
    
        return self.dfs(self.root, word, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
