# beats 99.8% runtime and 16% memory

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_list = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        ]
        
        result = ""
        
        for roman, value in roman_list:
            # append the Roman numeral to the result string and subtract the integer value from num
            while value <= num:
                result += roman
                num -= value
        
        return result