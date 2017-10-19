"""
https://leetcode.com/problems/reverse-vowels-of-a-string/description/


Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".


"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s = list(s)
        vowelList = []
        for i in xrange(len(s)):
            if s[i] in vowels:
                vowelList += s[i],
                s[i] = '_'
        for i in xrange(len(s)):
            if s[i] == '_':
                s[i] = vowelList.pop()
        return ''.join(s)

    def reverseVowelsOpt(self, s):
        vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)