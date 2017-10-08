class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = True if n & 1 == 1 else False
        n >>= 1
        while n > 0:
            if flag and (n & 1) == 1:
                return False
            if not flag and (n & 1) == 0:
                return False
            flag = not flag
            n >>= 1
        return True