class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        current_run = 0

        for c in s:
            if c == '1':
                current_run += 1
                count += current_run
            else:
                current_run = 0

        return count % MOD
