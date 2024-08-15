n = int(input())
k = int(input())
arr = [input().strip() for _ in range(n)]

check = [0]*n
temp = []

result = set()	# 중복된 조합 없애기

def card(N):
    if N == k:
        result.add(''.join(temp))
        return

    for i in range(n):
        if check[i]: 
        	continue
        check[i] = 1
        temp.append(arr[i])

        card(N+1)

        check[i] = 0
        temp.pop()
        
card(0)
print(len(result))