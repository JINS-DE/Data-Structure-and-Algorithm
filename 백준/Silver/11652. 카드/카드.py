import sys,heapq
input = sys.stdin.readline
N=int(input())
dic={}
li = [int(input()) for _ in range(N)]
heap=[]

for i in li :
    if dic.get(i)==None:
        dic[i]=1
    else:
        dic[i]+=1

for key,value in dic.items():
    heapq.heappush(heap,(-value,key))

val1,key1=heapq.heappop(heap)

min_li=[key1]
while heap :
    val2,key2=heapq.heappop(heap)
    if -val1 > -val2:
        break
    min_li.append(key2)

print(min(min_li))
