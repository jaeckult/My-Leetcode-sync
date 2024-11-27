class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftHalf = 0
        for i in range(len(nums)):
            print(leftHalf)
            rightHalf = sum(nums) - leftHalf -nums[i]
            print(rightHalf)
            if leftHalf == rightHalf:
                return i
            leftHalf+=nums[i]
        return -1
        