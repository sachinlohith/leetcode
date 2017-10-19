"""
https://leetcode.com/problems/merge-intervals/description/


Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x.start)
        res = []
        i = 0
        curL = intervals[0].start
        curR = intervals[0].end
        temp = [curL, curR]
        for interval in intervals[1:]:
            if temp[1] >= interval.start:
                temp[1] = max(temp[1], interval.end)
            else:
                res.append(temp)
                temp = [interval.start, interval.end]
        res.append(temp)
        return res

    def mergeOpt(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out