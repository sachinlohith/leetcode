"""
https://leetcode.com/problems/minimum-index-sum-of-two-lists/#/description
"""


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = []
        for x in list1:
            if x in list2:
                result.append((x, list1.index(x) + list2.index(x)))
        minVal = min(result, key=lambda x: x[1])[1]
        return map(lambda x: x[0], filter(lambda x: x[1] == minVal, result))
