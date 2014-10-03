from Queue import PriorityQueue

numbers = [5, 3, 6, 2, 6, 8, 0]
q = PriorityQueue()

for number in numbers:
    print 'put', number
    q.put(number)

print "size:", q.qsize()

while not q.empty():
    print 'pop', q.get()
    print "is empty:", q.empty()
