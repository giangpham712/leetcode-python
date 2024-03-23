from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        self.__backtrack(results, candidates[:], [], target)

        return results

    def __backtrack(self, results: List[List[int]], candidates: List[int], current: List[int], target: int):
        for idx, candidate in enumerate(candidates):
            if candidate == target:
                result = current[:]
                result.append(candidate)
                results.append(result)
            elif candidate < target:
                self.__backtrack(results, candidates[idx:], current + [candidate], target - candidate)