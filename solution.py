# Start of a Trie class
# The logic of the trie is that a node is the result of
# stepping through a string character by character.  When you
# reach the end of the string, you will be at the node pointed to
# by the last character.  _is_word tells you if that is the end
# of a word.
#
# The root is entirely consistent with this rule, as it is
# the node you reach having stepped through no characters.
# Its _children contains pointers to sub-tries corresponding
# to the starting letters in the string.


class Trie:

    # Add any attributes you want/need.
    # Any arguments you add to __init__() must follow the ones
    # defined below  and have a default value.

    def __init__(self, is_word):
        self._is_word = is_word
        self._children = {}  # children are a dictionary   
        
    def add(self, key):
        if key is None:
            raise ValueError
        
        if key == "":
            raise ValueError
        
        current = self
        
        for c in key:
            if c not in current._children:
                current._children[c] = Trie(is_word=False)
                
            current = current._children[c]
        
        if current._is_word is True:
            return False
        
        current._is_word = True           
        return True
            
    def add_keys(self, tuple_of_keys):
        if tuple_of_keys is None:
            raise ValueError
        
        # if not tuple_of_keys:
        #     raise ValueError
                
        count = 0
        
        for word in tuple_of_keys:
            current = self

            for c in word:
                if c not in current._children:
                    current._children[c] = Trie(is_word=False)
                    
                current = current._children[c]
            
            if current._is_word is False:
                current._is_word = True
                count += 1
                
        return count
            
    def remove(self, key):
        if key is None:
            raise ValueError
        
        if not key:
            raise ValueError
        
        current = self
                
        current._recursive_remove(current, key, 0)
                
    def _recursive_remove(self, current, key, index):
        current = self
        
        if index == len(key):
            if not current._is_word:
                return False
            
            current._is_word = False
            return len(current._children) == 0
        
        c = key[index]
        node_to_get = current._children.get(c)
        
        if node_to_get is None:
            return False
        
        # current._children[c] = self._recursive_remove(node_to_get, key, index + 1)
        del_node = self._recursive_remove(node_to_get, key, index + 1)

        if del_node is True:
            del current._children[c]
            return len(current._children) == 0 and not current._is_word
        
        return False
    
    def __contains__(self, key):
        if key is None:
            raise ValueError
        
        if key == "":
            raise ValueError
        
        current = self
        
        for c in key:
            if c not in current._children:
                return False
            else:
                current = current._children[c]
                
        return current._is_word
                
    def partial(self, prefix):
        if prefix is None:
            raise ValueError 
        
        words_with_prefix = []
        
        current = self
        
        if prefix == "":
            _prefix_search(current, [])
            return words_with_prefix
        
        for c in prefix:
            if c not in current._children:
                return words_with_prefix
            
            current = current._children[c]
            
        def _prefix_search(current, word_path):            
            if current._is_word:
                words_with_prefix.append(''.join(word_path))
                
            for c, node in current._children.items():
                _prefix_search(node, word_path + [c])
                    
        _prefix_search(current, list(prefix))
        
        return words_with_prefix
                
# https://www.youtube.com/watch?v=y3qN18t-AhQ
# https://www.youtube.com/watch?v=8mhw5WT2x0U
# https://www.geeksforgeeks.org/dsa/trie-insert-and-search/


if __name__ == "__main__":
    
    myTrie = Trie(is_word=False)
    
    # myTrie.add("dingo")
    # myTrie.add("dog")
    # myTrie.add("fork")

    # print(myTrie.__contains__("dingo"))
    # print(myTrie.__contains__("monster"))
    # print(myTrie.__contains__("dog"))
    # print(myTrie.__contains__("fork"))
    
    test_keys = ["for", "fork", "format", "forgo"]
    print(myTrie.add_keys(test_keys))

    # print(myTrie.__contains__("for"))
    # print(myTrie.__contains__("fork"))
    print(myTrie.__contains__("format"))
    # print(myTrie.__contains__("forgo"))
    
    myTrie.remove("format")
    print(myTrie.__contains__("format"))

    # myTrie.remove("dingo")
    # myTrie.remove("dog")
    # myTrie.remove("fork")
    # myTrie.remove("")
    
    # print(myTrie.partial(""))
    
    # print(myTrie.__contains__("dingo"))
    # print(myTrie.__contains__("monster"))
    # print(myTrie.__contains__("dog"))
    # print(myTrie.__contains__("fork"))
    
    # myTrie.add("fork")
    # myTrie.add("format")
    # myTrie.add("fortitude")
    # myTrie.add("for")
    # keyz = ["jane", "for", "john"]
    # keys = ["jane", "for", "john"]
    # keys2 = []
    
    # print(myTrie.add_keys(keyz))
    # print(myTrie.add_keys(keys))
    # print(myTrie.__contains__("jane"))
    
    # print(myTrie.partial("for"))
    # print(myTrie.partial())
