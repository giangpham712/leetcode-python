from typing import List


class Solution:
    def solve(self, words: List[str], k: int) -> List[str]:

        frequencies = {}

        for word in words:
            if word not in frequencies:
                frequencies[word] = 0

            frequencies[word] += 1

        rank: list[list] = [None for i in range(len(words))]

        for word, frequency in frequencies.items():
            if rank[frequency] is None:
                rank[frequency] = []

            rank[frequency].append(word)

        result = []

        for words in reversed(rank):

            if words is not None:
                words.sort()
                for word in words:
                    if k > 0:
                        result.append(word)
                        k -= 1
                    else:
                        break

        return result

        pass
