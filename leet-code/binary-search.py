"""
704. Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index,
otherwise return -1.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)

        middle_index = int(length / 2)

        max_value = middle_index

        check_index = middle_index

        while 0 <= check_index < length:
            num = nums[check_index]

            if num == target:
                return check_index

            if target < num:
                max_value = check_index

                check_index = int(check_index / 2)

                print(target, check_index, "Vou pra esquerda")
            else:
                check_index = int(check_index + (max_value - (check_index / 2)))
                print(target, check_index, "Vou pra direita")


        return -1


# print(Solution().search([-1, 0, 3, 5, 9, 12], 9))  # 4
# Explanation: 9 exists in nums and its index is 4

# print(Solution().search([-1, 0, 3, 5, 9, 12], 2))  # -1
# Explanation: 2 does not exist in nums so return -1

# print(Solution().search([-1, 0, 3, 5, 9, 12], 888888))  # -1
#
# print(Solution().search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 2))  # -1
print(Solution().search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 9))  # -1

"""
Max -> 10
Esq
5

Max - Current = 5
Novo Intervalo: Max - Current / 2

int(2.5) -> 2

Novo indice = Current + NovoIntervalo

Dir
"""

# Target: 15
# 10. Seria maior, iria pro segundo intervalo
# Qnd é maior, é o intervalo que eu estou mais a metade do que falta
# Estou em 10
# Length = 20 -> O que falta é max_value - 5 (atual / 2)
# Somo o resultado com o index atual e tenho um novo intervalo

# Length: 20
# Index do meio: 10
# Checa se o valor atual é igual ao que está
# Se o target for menor, vai pra esquerda
# Se o target for maior, vai pra direita
# Target é menor, pega o novo intervalo
# 10 / 2 -> 5
# Index do meio: 5
# Index do meio: 3
# Index do meio: 2

