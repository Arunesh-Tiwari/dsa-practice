from sortedcontainers import SortedList 

class SmallestInfiniteSet:

    def __init__(self):
        self.x = 1
        self.seen = SortedList()

    def popSmallest(self) -> int:
        if self.seen: return self.seen.pop(0)
        else: 
            self.x += 1
            return self.x - 1

    def addBack(self, num: int) -> None:
        if num < self.x and num not in self.seen: 
            self.seen.add(num)