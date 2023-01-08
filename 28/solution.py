# beats 92% runtime and 37% memory

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = haystack.find(needle)
        return index