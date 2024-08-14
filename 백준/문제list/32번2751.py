# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 머지 정렬로 구현
import sys
input=sys.stdin.readline
n=int(input())
a=[int(input()) for _ in range(n)]
# n=5
# a=[5,4,3,2,1]


def merge_sort(a):
    if len(a) <= 1:
        return a
    half = len(a)//2
    left_arr = merge_sort(a[:half])
    right_arr = merge_sort(a[half:])
    return merge(left_arr,right_arr)

def merge(left,right):
    tmp=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            i+=1
        else:
            tmp.append(right[j])
            j+=1
    tmp.extend(left[i:])
    tmp.extend(right[j:])
    return tmp

for i in merge_sort(a):
    print(i)

# 셰이커 정렬 : 시간초과
