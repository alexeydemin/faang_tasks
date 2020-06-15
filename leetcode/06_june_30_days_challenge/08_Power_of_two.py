class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bin(n)[2:].rstrip('0') == '1'

print(Solution().isPowerOfTwo(1024))