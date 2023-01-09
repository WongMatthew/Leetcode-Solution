# beats 99.77% runtime and 41.42% memory

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # base case if empty or 1 bracket
        if len(s) <= 1:
            return 0

        max_length = 0
        stack=[-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length=max(max_length, i-stack[-1])
        return max_length