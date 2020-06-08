class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        log_base_2 = log2(n)
        return math.ceil(log_base_2) == math.floor(log_base_2)
