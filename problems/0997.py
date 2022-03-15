from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n > 1:
                return -1
            return 1
        elif len(trust) == 1:
            return trust[0][1]

        relationMap = {}
        for i in range(1, n + 1):
            for x, y in trust:
                if y == i:
                    if relationMap.get(i):
                        relationMap[i].append(x)
                    else:
                        relationMap[i] = [x]

        candidate = None
        for k, v in relationMap.items():
            if len(set(v)) == n - 1:
                candidate = k

        if not candidate:
            return -1

        for k, v in relationMap.items():
            if k != candidate and candidate in v:
                return -1

        return candidate
