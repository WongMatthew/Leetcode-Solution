# Beats 97% runtime and 95.5% efficiency

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str not in hashmap:
                hashmap[sorted_str] = [i]
            else:
                hashmap[sorted_str].append(i)
            
        return([i for i in hashmap.values()]) 