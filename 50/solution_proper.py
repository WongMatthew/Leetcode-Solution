# beats 99.17% runtime and 97.43% memory
# Time: O(log n)
# Space: O(log n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        if not n:
            return 1
        # recursive case

        # if n is negative, return 1 divided by the power of x with positive n
        if n < 0:
            return 1 / self.myPow(x, -n)
        # if n is odd, return x multiplied by the power of x with (n-1)
        if n % 2:
            return x * self.myPow(x, n-1)
        # if n is even, return the power of xx with n/2
        return self.myPow(x*x, n/2)