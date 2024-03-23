from typing import List, Dict, Set

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        candidates.sort()

        self.__backtrack(results, candidates[:], [], target)

        return results

    def __backtrack(self, results: List[List[int]], candidates: List[int], current: List[int], target: int):
        useds = set()
        for idx, candidate in enumerate(candidates):
            if candidate in useds:
                continue

            useds.add(candidate)

            if candidate == target:
                result = current[:]
                result.append(candidate)

                results.append(result)
            elif candidate < target:
                self.__backtrack(results, candidates[(idx + 1):], current + [candidate], target - candidate)
