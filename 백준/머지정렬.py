a=[2,4,6,8,11,13]
b=[1,2,3,4,9,16,21]
c=[None]*(len(a)+len(b))

pa, pb, pc = 0, 0, 0 # 각 배열의 커서
na, nb, nc = len(a), len(b), len(c) # 각 배열의 원소의 수

while pa<na and pb <nb: # 배열의 커서가 인덱스 번호를 넘지 않을 때까지
    if a[pa] <= b[pb]: # b에 커서의 인덱스가 a의 커서보다 크거나 같을 때
        c[pc] = a[pa] # c 배열에 작은 값 a[pa] 삽입
        pa += 1 # pa 커서 값 증가
    else:
        # b에 커서 위치의 값이 a커서 위치의 값보다 작을 때
        c[pc] = b[pb] 
        pb+=1
    pc+=1

while pa < na: # a에 남은 원소가 있을 때
    c[pc] = a[pa] # c에 복사
    pa+=1
    pc+=1
while pb < nb : # b에 남은 원소가 있을 때
    c[pc] = b[pb]
    pb+=1
    pc+=1
print(c)

print('----------------------------------------------------')
# 리얼 병합 정렬 알고리즘
a=[5,8,4,2,6,1,3,9,7]
n = len(a)
buff=[None]*n

def merge_sort(a,left,right):
    # 파라미터 값의 의미
    # a : 병합 정렬할 배열
    # left : 배열의 맨 왼쪽 index 
    # right : 배열의 맨 오른쪽 index 
    if left < right:
        center = (left+right)//2
        merge_sort(a,left,center) # 재귀호출로 앞부분 정렬
        merge_sort(a,center+1,right) # 재귀호출로 뒷부분 정렬
        p=j=0
        i=k=left
        while i <= center:
            buff[p]=a[i]
            p+=1
            i+=1
        while i <= right and j<p:
            if buff[j] <= a[i]:
                a[k] = buff[j]
                j+=1
            else:
                a[k]=a[i]
                i+=1
            k+=1
        while j<p:
            a[k] = buff[j]
            k+=1
            j+=1
    print(buff)

merge_sort(a,0,n-1)
print(a)

def merge_sort(arr):
    # 배열의 길이가 1 이하이면 이미 정렬된 상태로 반환
    if len(arr) <= 1:
        return arr

    # 배열을 중간 기준으로 두 부분으로 분할
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 분할된 두 배열을 병합하여 반환
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # 두 리스트를 병합하는 과정
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # 남아 있는 요소를 추가
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# 예시
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("정렬된 배열:", sorted_arr)