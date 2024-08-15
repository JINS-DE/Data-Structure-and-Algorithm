import sys
input=sys.stdin.readline
class Stack:
    def __init__(self):
        self.array=[]
    def push(self,num):
        a=self.array
        a.append(num)       

    def pop(self):
        a=self.array
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop())
    def size(self):
        print(len(self.array))
    
    def empty(self):
        if len(self.array)==0:
            print(1)
        else:
            print(0)
    def top(self):
        if len(self.array)==0:
            print(-1)
        else:
            print(self.array[-1])
stack=Stack()
n=int(input())
for i in range(n):
    command=input().strip()
    if command[:4]=='push':
        _,num=command.split()
        stack.push(num)
    elif command=='top':
        stack.top()
    elif command=='pop':
        stack.pop()
    elif command=='size':
        stack.size()
    elif command=='empty':
        stack.empty()


