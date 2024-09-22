import math
from typing import List


class Solution:
    def solve(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        dist12 = Solution.__distance(p1, p2)
        dist34 = Solution.__distance(p3, p4)
        dist13 = Solution.__distance(p1, p3)
        dist24 = Solution.__distance(p2, p4)
        dist14 = Solution.__distance(p1, p4)
        dist23 = Solution.__distance(p2, p3)

        return (dist12 > 0 and dist13 > 0 and dist14 > 0 and
                dist12 == dist34 and
                dist13 == dist24 and
                dist14 == dist23 and
                (dist12 == dist13 or dist12 == dist14 or dist13 == dist14))

        pass

    def __distance(p1: List[int], p2: List[int]) -> float:
        return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))
