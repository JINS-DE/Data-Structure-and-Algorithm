import sys
min_val, max_val = map(int, sys.stdin.readline().split())
size = max_val - min_val + 1
memo = [True] * size

for i in range(2,int(max_val**0.5)+1):
    square = i * i
    start = ((min_val+square-1)//square)*square

    for j in range(start,max_val+1,square):
        memo[j-min_val]=False

print(sum(memo))