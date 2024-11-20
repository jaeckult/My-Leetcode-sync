class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        p_count = Counter(p)
        result = []
        for i in range(len(s)-k+1):
            window = s[i:i+k]
            if p_count == Counter(window):
                result.append(i)
        return result
