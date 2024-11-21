class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # if len(nums)<=k:
        #     return sum(nums)/len(nums)
        # start = 0
        # maxAv = 0
        # for i in range(k, len(nums)+1):
        #     currentAv = sum(nums[start:i])/k
        #     maxAv = max(maxAv, currentAv)
        #     start+=1
        # return maxAv

        if len(nums)<=k:
            return sum(nums)/len(nums)
        windowSum = sum(nums[:k])
        maxAverage = windowSum/k

        for i in range(k, len(nums)):
            windowSum = windowSum + nums[i] - nums[i-k]
            maxAverage = max(maxAverage, windowSum/k)
        return maxAverage