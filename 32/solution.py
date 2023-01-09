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
        stack=[-1] # stack to store '('
        # loop through string
        for i in range(len(s)):
            if s[i] == '(':
                # push '(' onto stack
                stack.append(i)
            # if s[i] = ')' remove '(' from stack
            else:
                stack.pop()
                # if stack is empty, push current index onto stack
                if not stack:
                    stack.append(i)
                # update max length
                else:
                    max_length=max(max_length, i-stack[-1])
        return max_length