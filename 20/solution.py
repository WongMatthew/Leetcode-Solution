# beats 75% runtime and 13% memory

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {"(":")", "[":"]", "{":"}"}
        stack = [s[0]]
        for i in range(1, len(s)):
            if len(stack) != 0 and brackets.get(stack[-1]) == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0