class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 0
        b = "".join("0" if x == "1" else "1" for x in bin(n)[2:])
        return int(b, 2)
