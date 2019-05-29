class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        start = 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen and seen[c] >= start:
                start = seen[c] + 1

            seen[c] = i
            maxlen = max(maxlen, i - start + 1)

        return maxlen
