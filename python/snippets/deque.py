from collections import deque

q = deque()

print 'append g, h, i'
q.append('g')
q.append('h')
q.append('i')
print q  # deque(['g', 'h', 'i'])

print 'appendleft f'
q.appendleft('f')
print q  # deque(['f', 'g', 'h', 'i'])

print 'pop', q.pop()  # i
print q  # deque(['f', 'g', 'h'])

print 'popleft', q.popleft()  # f
print q  # deque(['g', 'h'])
