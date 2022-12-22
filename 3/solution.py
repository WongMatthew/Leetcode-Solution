class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Set up a sliding window with two pointers, `left` and `right`
        left = 0
        right = 0
        # Create a set to store the characters in the current window
        window_chars = set()
        # Initialize a variable to store the maximum length of the substring
        max_length = 0
    
        # Loop as long as the right pointer is within the bounds of the string
        while right < len(s):
            # If the character at the right pointer is not in the window, add it to the window and move the right pointer forward
            if s[right] not in window_chars:
                window_chars.add(s[right])
                right += 1
            # If the character at the right pointer is already in the window, remove the character at the left pointer from the window and move the left pointer forward
            else:
                window_chars.remove(s[left])
                left += 1
            # Update the maximum length if the current window is longer
            max_length = max(max_length, right - left)
    
        # Return the maximum length
        return max_length