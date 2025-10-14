import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N=int(input())
n_arr = list(map(int,input().split()))
M=int(input())
m_arr = list(map(int,input().split()))
n_arr.sort()

def search_num(num):
    left = 0
    right = len(n_arr)-1
    if num<n_arr[left] or num>n_arr[right]:
        return 0
    
    while left<=right:
        mid = (left+right)//2
        if n_arr[mid]==num:
            return 1
        elif n_arr[mid]<num:
            left = mid+1
        else:
            right = mid-1  
    return 0
answer=[]
for m in m_arr:
    answer.append(search_num(m))
print(*answer)