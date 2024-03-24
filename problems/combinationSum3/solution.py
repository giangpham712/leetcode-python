from typing import List, Dict, Set

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        self.__backtrack(results, k, n)

        return results

    def __backtrack(self, results: List[List[int]], k, n):
        def find_missing(input):
            a = set(range(len(input)))
            for i in input:
                a.discard(i)

            return a.pop()

        pass
