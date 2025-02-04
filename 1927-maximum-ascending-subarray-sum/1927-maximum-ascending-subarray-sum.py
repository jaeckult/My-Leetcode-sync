from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]  # Initialize sum values
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # If ascending, add to current sum
                current_sum += nums[i]
            else:  # Otherwise, reset current sum
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        return max(max_sum, current_sum)  # Return the maximum sum found
