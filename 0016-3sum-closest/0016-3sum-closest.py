class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        result = sum(nums[:3])
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if abs(target - summ) < abs(diff):
                    diff = target - summ
                    result = summ
                if summ < target:
                    left += 1
                elif summ > target:
                    right -= 1
                else:
                    return summ
        
        return result
