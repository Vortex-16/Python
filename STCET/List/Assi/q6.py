#IMPLENET STACK & QUEQUE

# Stack using list
''''
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack:", stack)
print("Stack pop:", stack.pop())

# Queue using list
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue:", queue)
print("Queue dequeue:", queue.pop(0))
'''


# IMPLEMENT STACK & QUEUE

# Stack implementation using list
stack = []

# Push elements to stack
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushes:", stack)

# Pop element from stack
print("Popped from stack:", stack.pop())
print("Stack after pop:", stack)

# Queue implementation using list
from collections import deque

queue = deque()

# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueues:", list(queue))

# Dequeue element
print("Dequeued from queue:", queue.popleft())
print("Queue after dequeue:", list(queue))