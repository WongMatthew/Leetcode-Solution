class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first , last = strs[0], strs[-1]
        index = 0
        while index < len(first) and index < len(last):
            if first[index] != last[index]:
                break
            index+=1

        return first[:index]