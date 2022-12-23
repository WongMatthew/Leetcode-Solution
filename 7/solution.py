class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
        # Store the sign and make the integer positive
            sign = -1
            x = -x
        else:
            sign = 1
        # Convert the integer to a string and reverse the string using slicing
        s = str(x)[::-1]
        # Convert the reversed string back to an integer
        result = int(s)
        # If the result is outside the signed 32-bit integer range, return 0
        if result < -2147483648 or result > 2147483647:
            return 0
        # If the original integer was negative, negate the result and return it. Otherwise, return the result.
        return sign * result