# 1001/1083 test cases passed.

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        sign = 1
        sign_count = 0

        for c in s:
            # skip white space
            if c == " ":
                continue
            elif c == "+":
                sign = 1
                sign_count += 1
                if sign_count >= 2:
                    return 0
            elif c == "-":
                sign = -1
                sign_count += 1
                if sign_count >= 2:
                    return 0
            elif c == ".":
                return result * sign
            elif c.isdigit():
                result = result * 10 + int(c) 
            else:
                return sign * result

        if result * sign < -2147483648:
            return -2147483648
        elif result * sign > 2147483647:
            return 2147483647
        else:
            return sign * result