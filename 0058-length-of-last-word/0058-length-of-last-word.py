class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d = s.strip(" ")
        print(d)
        arr = d.split(" ")
        n = len(arr)
        print(arr)
        return len(arr[n-1])
# 4:15AM January 1, 2025. Abrehot Library.