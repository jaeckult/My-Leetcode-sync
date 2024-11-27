class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_so_far = 0
        current_sum = 0
        for num in nums:
            print(min_so_far)
            current_sum += num
            min_so_far = min(min_so_far, current_sum)

        return 1 - min_so_far