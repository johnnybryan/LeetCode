class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        list = [True] * n
        list[0] = list[1] = False
        for i in range(2, n):
            if list[i]:
                for j in range(i*i, n, i):
                    list[j] = False
        return sum(list)