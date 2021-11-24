from random import sample
from time import time
from P2 import Heap, MaxHeap, MinHeap
import heapq


class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO

class NaivePriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
    def put(self,val):
        if len(self.elements)>self.max_size:
            raise IndexError ('The maximun size has reached.')
        else:
            self.elements.append(val)
    def get(self):
        if len(self.elements) == 0:
            raise IndexError('The queue is empty.')
        else:
            min_ele = self.elements[0]
            min_i = 0
            for i,ele in enumerate(self.elements):
                if ele < min_ele:
                    min_ele = ele
                    min_i = i
            return self.elements.pop(min_i)

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError('The queue is empty.')
        else:
            min_ele = self.elements[0]
            min_i = 0
            for i,ele in enumerate(self.elements):
                if ele < min_ele:
                    min_ele = ele
                    min_i = i
            return self.elements[min_i]



class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
        self.heap = MinHeap(self.elements)

    def put(self,val):

        if len(self.elements)>self.max_size:
            raise IndexError ('The maximun size has reached.')
        else:
            self.heap.heappush(val)

    def get(self):
        return self.heap.heappop()



    def peek(self):
        if len(self.elements) == 0:
            raise IndexError('The queue is empty.')
        else:

            return self.heap.elements[0]



class PythonHeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)

    def put(self,val):

        if len(self.elements)>self.max_size:
            raise IndexError ('The maximun size has reached.')
        else:
            heapq.heappush(self.elements, val)


    def get(self):
        if len(self.elements) == 0:
            raise IndexError('The queue is empty.')
        else:
            return heapq.heappop(self.elements)



    def peek(self):
        if len(self.elements) == 0:
            raise IndexError('The queue is empty.')
        else:
            return self.elements[0]





if __name__ == '__main__':
    q = PythonHeapPriorityQueue(2)
    q.put(1)
    q.put(2)
    print(q.peek())
    print(q.get())
    print(q.get())
    # print(q.get())
