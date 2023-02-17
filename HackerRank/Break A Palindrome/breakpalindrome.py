'''
A palindrome reads the same from left to right as it does from right to left.
There is a palindrome which must be modified, if possible. Change exactly one character
of the string to any other lowercase English letter so that the resulting string is not a palindrome.
If there is no way to do this, return "IMPOSSIBLE".

The new string is lower alphabetically than the original string.

The new string is the lowest possible string that can be created by changing exactly one character in the original string.

The new string is not a palindrome.

Return the new string or "IMPOSSIBLE" if it is not possible to create a new string that is not a palindrome.
'''

def breakPalindrome(palindromeStr):
    if len(palindromeStr) == 1:
        return "IMPOSSIBLE"
    for i in range(len(palindromeStr)):
        if palindromeStr[i] != 'a':
            new_str = palindromeStr[:i] + 'a' + palindromeStr[i+1:]
            if new_str != new_str[::-1]:
                return new_str
    return "IMPOSSIBLE"