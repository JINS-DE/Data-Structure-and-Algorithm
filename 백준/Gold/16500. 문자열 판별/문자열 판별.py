s = input()  # 만들고자 하는 문자열 s를 입력받습니다.
n = int(input())  # 문자열 리스트 a의 개수 n을 입력받습니다.
a = [input() for i in range(n)]  # n개의 문자열을 입력받아 리스트 a에 저장합니다.

dp = [False for _ in range(len(s) + 1)]
dp[0]=True

for i in range(len(s)):
    if dp[i]==False:
        continue
    for word in a:
        if s[i:i+len(word)] == word:
            dp[i+len(word)]=True
print(int(dp[-1]))
