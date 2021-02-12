"""
420. Strong Password Checker

A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
"""


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'

        steps = 0

        length = len(password)

        need_add_length = 0
        need_remove_length = 0

        if length < 6:
            need_add_length = 6 - length

        if length > 20:
            need_remove_length = length - 20

        have_lower_letter = False
        have_upper_letter = False
        have_digit = False
        have_three_in_a_row = []

        for i, letter in enumerate(password):
            if not have_lower_letter and lower_letters.count(letter) > 0:
                have_lower_letter = True

            if not have_upper_letter and upper_letters.count(letter) > 0:
                have_upper_letter = True

            if not have_digit and digits.count(letter) > 0:
                have_digit = True

            if have_three_in_a_row.count(i) == 0 and length > i + 2 and password[i + 1] == letter and password[i + 2] == letter:
                have_three_in_a_row.append(i)
                have_three_in_a_row.append(i + 1)
                have_three_in_a_row.append(i + 2)

        if not have_lower_letter and need_add_length <= 1:
            steps += 1
            need_add_length -= 1

        if not have_upper_letter and need_add_length <= 1:
            steps += 1
            need_add_length -= 1

        if not have_digit and need_add_length <= 1:
            steps += 1
            need_add_length -= 1

        # 2
        # 3
        # 7

        if need_add_length > 0:
            steps += need_add_length

        if need_remove_length > 0:
            steps += need_remove_length

        three_in_a_row_replacements = len(have_three_in_a_row) / 3

        if three_in_a_row_replacements > steps:
            return int(three_in_a_row_replacements)


        return steps


# Tests

# print(Solution().strongPasswordChecker("a"))  # 5
# print(Solution().strongPasswordChecker("aA1"))  # 3
# print(Solution().strongPasswordChecker("1337C0d3"))  # 0
# print(Solution().strongPasswordChecker("aaab"))  # 3
# print(Solution().strongPasswordChecker("caaab"))  # 2
# print(Solution().strongPasswordChecker("cdaaa"))  # 2
# print(Solution().strongPasswordChecker("cdaaazxc"))  # 2
# print(Solution().strongPasswordChecker("abcde"))  # 2
# print(Solution().strongPasswordChecker("aaa111"))  # 2
# print(Solution().strongPasswordChecker("ABABABABABABABABABAB1"))  # 2
print(Solution().strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))  # 8 -> 23 letters
print(Solution().strongPasswordChecker("bbaaXaaCaa3aaCaacc2c"))  # 8 -> 23 letters

# Results for now:
# 41 / 50 test cases passed.

# Constrains

# 1 <= password.length <= 50
# password consists of letters, digits, dot '.' or exclamation mark '!'.
