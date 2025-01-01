class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for i in range(32):
            # Extract the least significant bit of n
            reversed_n <<= 1  # Shift reversed_n left by 1
            reversed_n |= (n & 1)  # Add the LSB of n to reversed_n
            n >>= 1  # Shift n right by 1 to process the next bit
        return reversed_n
#4:30 AM January 1, 2025. Abrehot Library.