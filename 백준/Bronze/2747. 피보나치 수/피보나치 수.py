import sys
n = sys.stdin.readline()
dp={}

def pibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    if n in dp:
        return dp[n]

    dp[n] = pibo(n-1)+pibo(n-2)
    return dp[n]
    

print(pibo(int(n)))