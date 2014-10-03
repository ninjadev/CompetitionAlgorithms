from Queue import PriorityQueue

numbers = [5, 3, 6, 2, 6, 8, 0]
q = PriorityQueue()

for number in numbers:
    priority = -number
    print 'put', number
    q.put((priority, number))

print "size:", q.qsize()

while not q.empty():
    print 'pop', q.get()[1]
    print "is empty:", q.empty()
