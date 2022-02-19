class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        i = num//3
        if (i-1)+i+(i+1) == num:
            return [i-1, i, i+1]
        return []