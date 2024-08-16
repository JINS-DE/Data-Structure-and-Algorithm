import sys
from collections import deque

input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, num):
        self.queue.append(num)
    
    def pop(self):
        if not self.queue:
            print(-1)
        else:
            print(self.queue.popleft())
    
    def size(self):
        print(len(self.queue))
    
    def empty(self):
        if not self.queue:
            print(1)
        else:
            print(0)
    
    def front(self):
        if not self.queue:
            print(-1)
        else:
            print(self.queue[0])
    
    def back(self):
        if not self.queue:
            print(-1)
        else:
            print(self.queue[-1])

queue = Queue()
n = int(input())
for i in range(n):
    command = input().strip()
    if command.startswith('push'):
        _, num = command.split()
        queue.push(num)
    elif command == 'front':
        queue.front()
    elif command == 'pop':
        queue.pop()
    elif command == 'size':
        queue.size()
    elif command == 'empty':
        queue.empty()
    elif command == 'back':
        queue.back()
