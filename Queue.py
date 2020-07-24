
from collections import deque
class Queue():
    def __init__(self):
        self.queue = deque()
        self.size = 0
    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1
    def dequeue(self, item):
        if self.size > 0:
            self.size -= 1
            return self.queue.popleft()
        else: 
            return None
    def peek(self):
        if self.size > 0:
            ret_val = self.queue.popleft()
            self.queue.appendleft(ret_val)
            return ret_val
        else:
            return None
    def get_size(self):
        return self.size

myQueue = Queue()
myQueue.enqueue(5)
myQueue.enqueue(15)
myQueue.enqueue(20)
myQueue.enqueue(25)
myQueue.enqueue(35)
print(myQueue.get_size())
myQueue.peek()
print(myQueue.dequeue(15))
print(myQueue.dequeue(5))
print(myQueue.get_size())
myQueue.peek()








