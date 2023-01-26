# beats 97% of runtime and 98% of memory

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        if not strs:
            return ""

        strs.sort()
        prefix = strs[0]

        # iterate through 1st string
        for i, c in enumerate(prefix):
            # i >= len(strs[-1])  --> breaks b/c the string is too short compared to size of prefix
            # strs[-1][i] != c  --> check if current value is in the same position as the one its being compared to
            if i >= len(strs[-1]) or strs[-1][i] != c:
                prefix = prefix[:i]
                break
        return prefix