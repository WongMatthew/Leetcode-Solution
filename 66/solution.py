# beats 93% runtime and 96% memory

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # initialize empty string
        string = ""
        # iterate through digits
        for num in digits:
            # add each digit to string
            string += str(num)
        
        # convert string to int and add 1
        res = int(string)+1

        # convert int to string and then to list
        final_string = [int(d) for d in str(res)]
        return final_string