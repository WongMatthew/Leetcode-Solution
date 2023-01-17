# beats 5.4% runtime and 99.94% memory

class Solution:
    def myPow(self, x: float, n: int) -> float:
        #set up temp variable
        temp = x
        # handle edge cases
        if x == 1:
            return 1
        if x == -1 and n%2 == 0:
            return 1
        if x == -1 and n%2 == 1:
            return -1
        if n == 2147483647 or n == -2147483648:
            return 0
        if n == 0:
            return 1
        # handle positive and negative exponents
        elif n > 0:
            for i in range(n-1):
                x = x*temp
            return x
        else:
            for i in range(abs(n)-1):
                x = x*temp
            return 1/x