from math import floor
from typing import List

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size



    def build_heap(self) -> None:
        for idx in range(floor(self.size//2)-1, -1, -1):
            self.heapify(idx)

    def heappush(self, key: int) -> None:
        self.elements.append(key)
        self.build_heap()


    def heappop(self) -> int:
        if len(self.elements) != 0:
            return self.elements.pop(0)
        else:
            raise IndexError('Cannot get the minimum element in array since it does not exist.')
        self.build_heap()

    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

class MinHeap(Heap):
    def __init__(self, array: List[int]):
        super().__init__(array)

    def heapify(self, idx: int) -> None:

        l = self.left(idx)
        r = self.right(idx)
        if l < self.size and self.compare(self.elements[l],self.elements[idx]):
            smallest = l
        else:
            smallest = idx
        if r < self.size and self.compare(self.elements[r],self.elements[smallest]):
            smallest = r
        if smallest != idx:
            self.swap(idx, smallest)
            self.heapify(smallest)

    def compare(self, a: int, b: int) -> bool:
        if a < b:
            return True
        else:
            return False


class MaxHeap(Heap):
    def __init__(self, array: List[int]):
        super().__init__(array)

    def heapify(self, idx: int) -> None:

        l = self.left(idx)
        r = self.right(idx)
        if l < self.size and self.compare(self.elements[l],self.elements[idx]):
            largest = l
        else:
            largest = idx
        if r < self.size and self.compare(self.elements[r],self.elements[largest]):
            largest = r
        if largest != idx:
            self.swap(idx, largest)
            self.heapify(largest)

    def compare(self, a: int, b: int) -> bool:
        if a > b:
            return True
        else:
            return False

if __name__=='__main__':
    h = MinHeap([-1, 0, 0, 15, 23, 1, 2, 3])  # The heap tree will be built during initialization
    print(h)
    h.heappush(4)
    h.heappop()
    print(h)