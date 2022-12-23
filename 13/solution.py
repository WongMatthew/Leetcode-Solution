# beats 82% of runtime and 61% of memory

class Solution(object):
    def romanToInt(self, s):
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0

        for i in range(len(s)):
            # Get the integer value of the current character
            value = roman_dict[s[i]]
            # If current has a smaller int value than next, subtract the current integer value from the result var
            if i < len(s) - 1 and roman_dict[s[i + 1]] > value:
                result -= value
            else:
                result += value
        
        return result