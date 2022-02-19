class Solution:
    def maximumEvenSplit(self, fin: int) -> List[int]:
        if fin % 2:
            return []
        fin //= 2
        cur = 0
        arr = []
        i = 1
        while i + cur <= fin:
            arr.append(i)
            cur += i
            i += 1
        arr[-1] += fin - cur
        arr = [i * 2 for i in arr]
        return arr
        