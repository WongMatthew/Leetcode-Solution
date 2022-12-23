class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        max_p = ""
        # Iterate over each character in the string
        for i in range(len(s)):
            print("i-loop iteration" + str(i))
            # Iterate over two positions: i and i + 1
            for j in range(i, i + 2):
                print("j-loop iteration " + str(j) + ": "+ str(i) + str(j))
                # Initialize pointers b and e to the current position
                b = i
                e = j
                print(s[b] + s[e])
                # Keep moving the pointers outward until they reach characters that are not equal, or until they go out of bounds
                while b >= 0 and e < len(s) and s[b] == s[e]:
                    b -= 1
                    e += 1
                # Calculate the length of the palindromic substring
                l = e - b - 1
                # If the length is greater than the maximum length found so far, update the maximum length and palindromic substring
                if l > max_len:
                    max_len = l
                    max_p = s[b + 1 : e]
                    print(l)
        return max_p