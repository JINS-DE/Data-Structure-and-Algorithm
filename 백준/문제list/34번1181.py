# # 시간초과 답도 틀린듯 확인해야함
# import sys
# input=sys.stdin.readline
# n=int(input())
# a=list(set(input().strip() for _ in range(n)))

# for i in range(1,len(a)):
#     for j in range(len(a)-i-1):
#         if len(a[j]) > len(a[j+1]) or (len(a[j]) == len(a[j+1]) and a[j] > a[j+1]):
#             a[j],a[j+1]=a[j+1],a[j]

# for i in a:
#     print(i)  

# 머지정렬로 해결
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # 두 리스트를 병합하는 과정
    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]) or (len(left[i]) == len(right[j]) and left[i] < right[j]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # 남은 요소를 추가
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list


# 연우님 코드리뷰 python으로는 시간초과 pypy로 돌려야함
import sys
n = int(input())
words = []
for _ in range(n):
    word = sys.stdin.readline()
    if word not in words:
        words.append(word)
arr = []
for i in range(len(words)):
    max_word = words[0]
    index = 0
    for j in range(1,len(words)-i):
        if (len(words[j]) == len(max_word) and words[j] > max_word) or len(words[j]) > len(max_word):
            max_word = words[j]
            index = j
    tmp = words[len(words)-i-1]
    words[len(words)-i-1] = words[index]
    words[index] = tmp
for word in words:
    sys.stdout.write(word)
