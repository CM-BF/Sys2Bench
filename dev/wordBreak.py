from typing import List

class TrieNode:
    def __init__(self, char):
        self.isWord = False
        self.children = dict()
        self.char = char

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        root = TrieNode(None)
        for word in wordDict:
            curr = root
            print(word)
            for i, c in enumerate(word):
                print(c)
                if c not in curr.children:
                    print("Adding")
                    curr.children[c] = TrieNode(c)
                curr = curr.children[c]
            curr.isWord = True
            print(i, curr.isWord)

        for word in wordDict:
            curr = root
            for c in word:
                curr = curr.children[c]
            if not curr.isWord:
                print(f"{word} is not in the Trie!!!!")

        def dfs(node, pos):
            if pos == len(s) - 1:
                return node.isWord
            pos += 1
            c = s[pos]
            state = f"{c}, {pos}, {node.char}"
            print(f"Curr char: {state}")
            if node.isWord:
                print(f"Found word: {state}")
                if dfs(node=root, pos=pos - 1):
                    return True
            if c not in node.children:
                print(f"Not in children: {state}")
                return False
            if dfs(node=node.children[c], pos=pos):
                return True
            print(f"Returning false {state}")
            return False

        return dfs(node=root, pos=-1)        
    
if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    assert sol.wordBreak(s, wordDict)
    
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    assert sol.wordBreak(s, wordDict)

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    assert not sol.wordBreak(s, wordDict)

    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]
    assert sol.wordBreak(s, wordDict)
