"""
https://leetcode.com/problems/decode-string/description/


Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                curNum = ''
                while i < len(s) and s[i].isdigit():
                    curNum += s[i]
                    i += 1
                stack.append(int(curNum))
            elif s[i] == '[':
                stack.append(s[i])
                i += 1
            elif s[i].isalpha():
                curString = ''
                while i < len(s) and s[i].isalpha():
                    curString += s[i]
                    i += 1
                stack.append(curString)
            else:
                run = ''
                while stack and stack[-1] != '[':
                    run = stack.pop() + run
                stack.pop()
                run = run * stack.pop()
                stack.append(run)
                i += 1
        return ''.join(stack)

