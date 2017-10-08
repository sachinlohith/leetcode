"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
Q. What if the given array is already sorted? How would you optimize your algorithm?

If both arrays are sorted, I would use two pointers to iterate, which somehow resembles the merge process in merge sort.

Q. What if nums1's size is small compared to nums2's size? Which algorithm is better?

Suppose lengths of two arrays are N and M, the time complexity of my solution is O(N+M) and the space complexity if O(N) considering the hash. So it's better to use the smaller array to construct the counter hash.

Well, as we are calculating the intersection of two arrays, the order of array doesn't matter. We are totally free to swap to arrays.

Q. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Divide and conquer. Repeat the process frequently: Slice nums2 to fit into memory, process (calculate intersections), and write partial results to memory.
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c1, c2 = Counter(nums1), Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])
