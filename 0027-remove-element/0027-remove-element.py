class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            while left < right and nums[right] == val:
                right -= 1
            
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            
            left += 1
        return right + 1
