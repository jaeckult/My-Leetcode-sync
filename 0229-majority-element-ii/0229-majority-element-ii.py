class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        print(counter)
        req = len(nums)//3
        result = []
        for i in counter:
            if counter[i]>req:
                result.extend([i])
        return result