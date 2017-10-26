"""
https://leetcode.com/problems/add-bold-tag-in-string/description/


Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:
Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].

"""


class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        N = len(s)
        boolArray = [False] * N
        for word in dict:
            D = len(word)
            for i in xrange(0, N - D + 1):
                if s[i:i + D] == word:
                    for j in xrange(i, i + D):
                        boolArray[j] = True
        res = []
        i = 0
        while i < N:
            if boolArray[i]:
                cur = list('<b>')
                while i < N and boolArray[i]:
                    cur.append(s[i])
                    i += 1
                cur.extend(list('</b>'))
                res.extend(cur)
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)