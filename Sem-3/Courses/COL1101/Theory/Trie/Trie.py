class TrieNode:
    def __init__(self):
        self.child=[None]*26
        self.leaf=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,key):
        curr=self.root

        for c in key:
            idx=ord(c)-ord('a')

            if curr.child[idx] is None:
                curr.child[idx]=TrieNode()

            curr=curr.child[idx]

        curr.leaf=True

    def search(self,key):
        curr=self.root

        for c in key:
            idx=ord(c)-ord('a')
            if curr.child[idx] is None:
                return False

            curr=curr.child[idx]
        return curr.leaf

    def ispre(self,prefix):
        curr=self.root

        for c in prefix:
            idx=ord(c)-ord('a')

            if curr.child[idx] is None: return False
            curr=curr.child[idx]

        return True
    