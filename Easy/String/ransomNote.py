"""
https://leetcode.com/problems/ransom-note/#/description

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for x in ransomNote:
            if x not in magazine:
                return False
            magazine.remove(x)
        return True

    def canConstructOpt(self, ransomNote, magazine):
        from collections import defaultdict
        table = defaultdict(int)
        for x in magazine:
            table[x] += 1
        for x in ransomNote:
            if x not in table or table[x] - 1 < 0:
                return False
            table[x] -= 1
        return True
