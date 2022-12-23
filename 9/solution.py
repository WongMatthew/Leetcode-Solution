# beat 85% runtime and 88% memory

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        x_rev = list(str(x))
        x_rev.reverse()
        if list(str(x)) == x_rev:
            return True
        return False    