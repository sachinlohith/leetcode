"""
Implement pow(x, n).
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            n = abs(n)
            x = (1.0/x)
        return self.myPow(x*x, n/2) if n % 2 == 0 else x * self.myPow(x*x, n/2)

if __name__ == "__main__":
    sol = Solution()
    print sol.myPow(3.5, 3)
    print sol.myPow(4, 0)
    print sol.myPow(4, -1)
