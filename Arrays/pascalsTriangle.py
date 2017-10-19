"""
https://leetcode.com/problems/pascals-triangle/discuss/


Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        start = 1
        for i in xrange(1, numRows):
            nextList = [0] * (i + 1)
            prevList = res[i - 1]
            for j in xrange(len(nextList)):
                if j == 0 or j == i:
                    nextList[j] = 1
                else:
                    nextList[j] = prevList[j - 1] + prevList[j]
            res += nextList,
        return res

    def generateOpt(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]