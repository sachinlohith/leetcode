"""
https://leetcode.com/problems/sentence-screen-fitting/description/


Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
"""


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        umap = {}
        num, n = 0, len(sentence)
        for _ in xrange(rows):
            start = num % n
            if start in umap:
                num += umap[start]
            else:
                cnt, length = 0, 0
                i = start
                while length < cols and length + len(sentence[i]) <= cols:
                    length += len(sentence[i]) + 1
                    cnt += 1
                    i = (i + 1) % n
                num += cnt
                umap[start] = cnt
        return num / n
