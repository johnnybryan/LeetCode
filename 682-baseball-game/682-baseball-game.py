class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for i in range(len(ops)):
            if ops[i] == '+':
                record.append(record[-1]+record[-2])
            elif ops[i] == 'D':
                record.append(2*record[-1])
            elif ops[i] == 'C':
                record.pop()
            else:
                record.append(int(ops[i]))
        return sum(record)
                