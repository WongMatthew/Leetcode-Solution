# beat 95% runtime and 65% memory

class Solution(object):
    def isPalindrome(self, x): 
        if x < 0:
            return False
        if x < 10:
            return True
        s = str(x)
        i = 0
        j = len(s)-1
        while (i < j):
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True