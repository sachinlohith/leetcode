class solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        charMap = {}
        left = 0
        best = 0
        for i in xrange(len(s)):
            if s[i] in charMap:
                charMap[s[i]] += 1
            else:
                charMap[s[i]] = 1
            while len(charMap) > k:
                charMap[s[left]] -= 1
                if charMap[s[left]] == 0:
                    del charMap[s[left]]
                left += 1
            best = max(best, i - left + 1)
        return best
