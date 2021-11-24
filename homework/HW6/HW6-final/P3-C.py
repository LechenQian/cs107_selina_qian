from random import sample
from time import time
from P2 import Heap, MaxHeap, MinHeap
from P3 import PriorityQueue, NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue
import matplotlib.pyplot as plt
import heapq


def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists):
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i))

    return merged


def generatelists(n, length=20, dictionary_path='../data/words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end = time()
            timeaccum += end - start
        elapsed.append(timeaccum / n_average)
    return elapsed


runtimes = []
pqclasses = [NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue]
for pqclass in pqclasses:
    runtime = timeit(pqclass=pqclass)
    runtimes.append(runtime)
    print(runtime)
ns = (10, 20, 50, 100, 200, 500)

plt.figure(figsize=(10,10))
plt.plot(ns, runtimes[0], label='NaivePriorityQueue',alpha = 0.5)
plt.plot(ns, runtimes[1], label='HeapPriorityQueue',alpha = 0.5)
plt.plot(ns, runtimes[1], label='PythonHeapPriorityQueue',alpha = 0.5)
plt.legend()
plt.title('the running time of mergesortedlists on different number of list using three sort methods')
plt.xlabel('numbers of lists')
plt.xlim([0, 500])
plt.ylabel('running time(s)')
plt.savefig('P3-C.png')
