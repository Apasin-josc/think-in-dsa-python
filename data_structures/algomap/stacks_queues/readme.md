## stacks (LIFO - Last In First Out) - good to use dynamic arrays

### .append
```
stack = []
stack.append(5)
stack.append(10)
stack.append(15)
```
### .pop
```
stack.pop()
```

### .peek 
```
stack[-1] #[10] 
```

### .isEmpty
```
if stack:
    True
```
## queues (FIFO - First In First Out) - good to use doubly linked list

### .enqueue (add element to the right)
```
from collections import deque

q = deque()
q.append(5)
q.append(6)
print(q) # deque([5,6])
```
### .dequeue (remove element from the left)
```
q.popleft() #5
```

### .peek from left side
```
q[0]
```

### .peek from right side
```
q[-1]
```