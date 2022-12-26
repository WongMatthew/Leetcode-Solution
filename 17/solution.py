# beats 86% runtime and 42% memory

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = {
             '0': '0',
             '1': '1',
             '2': 'abc',    
             '3': 'def', 
             '4': 'ghi', 
             '5': 'jkl',   
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxzy'
        }
        r = []
        for c in digits:
            if not r:
                for i in m[c]:
                    r.append(i)
            else:
                t = []
                for k in r:
                    for i in m[c]:
                        t.append(k+i)
                r = t
        return r