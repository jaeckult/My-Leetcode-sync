import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = list(itertools.permutations(nums))
        return permutations
