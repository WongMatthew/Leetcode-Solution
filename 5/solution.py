class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        max_p = ""
        for i in range(len(s)):
            for j in range(i, i + 2):
                b = i
                e = j
                while b >= 0 and e < len(s) and s[b] == s[e]:
                    b -= 1
                    e += 1
                l = e - b - 1
                if l > max_len:
                    max_len = l
                    max_p = s[b + 1 : e]
        return max_p