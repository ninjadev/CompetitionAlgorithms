import heapq

def heapsort(array):
    heap = []
    for value in array:
        heapq.heappush(heap, value)

    return [heapq.heappop(heap) for i in range(len(heap))]

# This also works with tuples
print heapsort([1,-5,3,6,2,4,3,1,4,5,2,3,3])
