class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        n = int(str(abs(x))[::-1])
        if n.bit_length() > 31:
            return 0
        elif x < 0:
            return n * -1
        return n
