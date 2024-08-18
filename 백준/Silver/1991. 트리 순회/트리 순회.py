import sys
input = sys.stdin.readline
n=int(input())
graph={}
for i in range(n):
    p,c1,c2=input().split()
    graph[p]=[c1,c2]

def pre_recursive(parent):
    if parent!='.':
        print(parent,end='')
        pre_recursive(graph[parent][0])
        pre_recursive(graph[parent][1])

def mid_recursive(parent):
    if parent!='.':
        mid_recursive(graph[parent][0])
        print(parent,end='')
        mid_recursive(graph[parent][1])

def back_recursive(parent):
    if parent!='.':
        back_recursive(graph[parent][0])
        back_recursive(graph[parent][1])
        print(parent,end='')

pre_recursive('A')
print()
mid_recursive('A')
print()
back_recursive('A')
