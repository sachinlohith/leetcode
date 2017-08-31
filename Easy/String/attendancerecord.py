"""
https://leetcode.com/problems/student-attendance-record-i/description/

You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = 0
        acount = 0
        for x in s:
            if x == 'L' and flag == 2:
                return False
            elif x == 'L':
                flag += 1
            elif x == 'A':
                acount += 1
                if acount > 1:
                    return False
                flag = 0
            else:
                flag = 0
        return True

    def checkRecordOpt(self, s):
        return not (s.count('A') > 1 or 'LLL' in s)
