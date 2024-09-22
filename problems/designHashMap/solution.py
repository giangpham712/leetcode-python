class Solution:
    def solve(self):
        pass


class MyHashMap:

    numOfBuckets = 100

    def __init__(self):
        self.buckets = [[] for _ in range(self.numOfBuckets)]
        pass

    def put(self, key: int, value: int) -> None:
        hash = key % self.numOfBuckets
        bucket = self.buckets[hash]
        entry = next((x for x in bucket if x[0] == key), None)

        if entry != None:
            entry[1] = value
        else:
            bucket.append([key, value])

        pass

    def get(self, key: int) -> int:
        hash = key % self.numOfBuckets
        bucket = self.buckets[hash]
        entry = next((x for x in bucket if x[0] == key), None)

        if entry != None:
            return entry[1]
        else:
            return -1

    def remove(self, key: int) -> None:
        hash = key % self.numOfBuckets
        bucket = self.buckets[hash]
        entry = next((x for x in bucket if x[0] == key), None)

        if entry != None:
            bucket.remove(entry)