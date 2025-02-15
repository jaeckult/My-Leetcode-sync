class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key=lambda x: ''.join(sorted(x)))
        result = []
        left = 0
        while left < len(strs):
            right = left
            while right < len(strs) and sorted(strs[left]) == sorted(strs[right]):
                right += 1
            result.append(strs[left:right])  
            left = right
        return result