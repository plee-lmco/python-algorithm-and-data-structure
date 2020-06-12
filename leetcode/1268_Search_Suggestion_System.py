'''
1268. Search Suggestions System Medium
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
'''
class Node:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self, node):
        self.root = node
        
    def insert(self, word):
        curr_node = self.root
        
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = Node()
   
            curr_node = curr_node.children[letter]
            curr_node.words.append(word)
            
    # Search for the word in trie
    def search(self, word):
        # Set to trie's root
        curr_node = self.root
        
        # Loop through all letters
        for letter in word:
            # Check if letter in children map
            if letter in curr_node.children:
                # Letter exist, set to current node
                curr_node = curr_node.children[letter]
            else:
                # No match, return empty array
                return []
        # Return all words
        return curr_node.words
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #return self.simpleSort(products, searchWord)
        return self.use_trie(products, searchWord)
        pass
    
    def use_trie(self, products, searchWord):
        result_list = []
        root = Node()
        # Use tree trie solution 
        # Create tree struction with product
        word_trie = Trie(root)
        
        # Sort the products
        products.sort()
        for product in products:
            word_trie.insert(product)
        
        # For each additional letter, run search
        for index in range(len(searchWord)):
            prefix_to_search = searchWord[:index+1]
            result_list.append(word_trie.search(prefix_to_search)[:3])
        return result_list
        
    # Simple sort without use of Trie
    def simpleSort(self, products, searchWord):
        all_results = []
        products.sort()
        
        for index, char in enumerate(searchWord):
            results_list = []
            for p in products:
                if len(p) > index and p[:index+1] == searchWord[:index+1]:
                    results_list.append(p)
            all_results.append(results_list[:3])
        return all_results
