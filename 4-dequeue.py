from collections import deque

# Initializing a queue

q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\n Elements dequeued from the queue")

print(q.pop())

#print(q.popleft())