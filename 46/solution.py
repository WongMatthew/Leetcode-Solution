# beats 67% runtime and 97% memory

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Initialize stack with input list and empty path
        stack = [(nums, [])]
        # Initialize empty list to store permutations
        res = []
        # While stack is not empty
        while stack:
            # Pop top element off stack
            nums, path = stack.pop()

            # print("----Pop Stack----")
            # print(stack)

            # If list of numbers is empty, add current path to result list
            if not nums:
                res.append(path)
                # print("----Updated Res----")
                # print(res)
            # Iterate through numbers in list
            for i in range(len(nums)):
                # Create new list with current number removed
                newNums = nums[:i] + nums[i+1:]

                # print("----DFS----")
                # print(newNums)

                # Append current number to path
                stack.append((newNums, path+[nums[i]]))
                
                # print("----App Stack----")
                # print(stack)
        
        # Return result list
        return res