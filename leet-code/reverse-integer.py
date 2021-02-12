"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], then return 0.

signed int 32 bit: [-2147483648 to 2147483647]
"""


class Solution:
    def reverse(self, x: int) -> int:
        reverse_number = (str(x))[::-1]

        if reverse_number[-1] == "-":
            reverse_number = "-" + reverse_number[:-1]

        reverse_number = int(reverse_number)

        if reverse_number <= -2147483648 or reverse_number >= 2147483647:
            return 0

        return reverse_number


# Tests

print(Solution().reverse(123))  # 321
print(Solution().reverse(-123))  # -321
print(Solution().reverse(120))  # 21
print(Solution().reverse(1534236469))  # 0 -> mine: 9646324351

print(Solution().reverse(0))  # 0
print(Solution().reverse(2147483648))  # 0
print(Solution().reverse(-2147483649))  # 0
