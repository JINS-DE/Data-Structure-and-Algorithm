N,K = map(int,input().split())
temps = list(map(int, input().split()))
current_sum = sum(temps[:K])
max_sum = current_sum

for i in range(K, N):
    current_sum += temps[i] - temps[i-K]
    max_sum = max(max_sum, current_sum)

print(max_sum)