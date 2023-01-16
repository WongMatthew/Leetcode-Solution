class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for num in digits:
            string += str(num)

        res = int(string)+1

        final_string = [int(d) for d in str(res)]
        return final_string