import heapq
l1=[10,11,12,13,32,7,89,6,9]
heapq.heapify(l1)
print(list(l1))
heapq.heappush(l1,8)
print(list(l1))
print(heapq.heappop(l1))