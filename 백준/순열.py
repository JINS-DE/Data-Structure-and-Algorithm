A = ['1', '2', '3', '4', '5', '6']
N = 3
check = [0] * len(A)  # check 배열 크기는 6
arr = [0] * N 
li = []

def permutations(level):
    if level == N:
        li.append(''.join(arr))
        return
    for i in range(len(A)):
        if check[i]:
            continue
        check[i] = 1
        arr[level] = A[i]
        permutations(level + 1)
        check[i] = 0

permutations(0)
print(li)

permutations(0)
level=0
i=0
check=[1,0,0,0,0,0]
arr = [1,0,0]
li = []

permutations(1)
i=1
level=1
check=[1,1,0,0,0,0]
arr = [1,2,0]

check=[1,0,0,0,0,0]

i=2
level=1
check=[1,0,1,0,0,0]
arr=[1,3,0]

i=3
level=1
check=[1,0,0,1,0,0]
