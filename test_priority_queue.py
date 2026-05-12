'''
Tests for Priority Queue.
'''

from priority_queue import PriorityQueue

pq = PriorityQueue()

# Test 1: Queue starts empty
assert pq.is_empty() == True
print('Test 1 passed: queue starts empty')

# Test 2: Insert one ticket
pq.insert('Ana Garcia', 'Cannot login', 2)
assert len(pq) == 1
print('Test 2 passed: insert one ticket')