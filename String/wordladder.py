"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
    For example,

    Given:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
        return its length 5.

    Note:
        Return 0 if there is no such transformation sequence.
        All words have the same length.
        All words contain only lowercase alphabetic characters.
        You may assume no duplicates in the word list.
        You may assume beginWord and endWord are non-empty and are not the same.
"""
import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        Use BFS to solve the problem
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for index in xrange(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:index] + char + word[index+1:]
                    if newWord in wordList:
                        wordList.remove(newWord)
                        queue.append([newWord, length + 1])
        return 0


if __name__ == "__main__":
    sol = Solution()
    print sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    print sol.ladderLength("a", "c", ["a", "b", "c"])
