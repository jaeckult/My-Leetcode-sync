class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        result = []
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue  
            middle, right = left + 1, len(nums) - 1 
            while middle < right:
                current_sum = nums[left] + nums[middle] + nums[right]
                if current_sum == 0:
                    result.append([nums[left], nums[middle], nums[right]])
                    while middle < right and nums[middle] == nums[middle + 1]:
                        middle += 1
                    while middle < right and nums[right] == nums[right - 1]:
                        right -= 1
                    middle += 1
                    right -= 1
                elif current_sum < 0:
                    middle += 1
                else:
                    right -= 1
        return result
