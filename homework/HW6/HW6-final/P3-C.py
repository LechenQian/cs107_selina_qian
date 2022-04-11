from random import sample
from time import time
from P2 import Heap, MaxHeap, MinHeap
from P3 import PriorityQueue, NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue, mergesortedlists, timeit, generatelists
import matplotlib.pyplot as plt
import heapq

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
plt.plot(ns, runtimes[2], label='PythonHeapPriorityQueue',alpha = 0.5)
plt.legend()
plt.title('the running time of mergesortedlists on different number of list using three sort methods')
plt.xlabel('numbers of lists')
plt.xlim([0, 500])
plt.ylabel('running time(s)')
plt.savefig('P3-C.png')
