# 208. Implement Trie (Prefix Tree) Medium
# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
# Note:
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
class Node:
    def __init__(self, letter=''):
        self.word = ''
        self.children = {}

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                node = Node(letter)
                curr.children[letter] = node
                curr = node
        curr.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            else:
                curr = curr.children[letter]
        if curr.word == word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            else:
                curr = curr.children[letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)