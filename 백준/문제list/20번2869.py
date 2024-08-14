'''땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.'''

#1 카운트 세기 while문 사용 : X 시간초과 
# A,B,V=map(int,input().split())
# goal=0
# cnt=0
# while True:
#     goal+=A
#     if goal>=V:
#         cnt+=1
#         break
#     goal-=B
#     cnt+=1
# print(cnt)
    
#2 다른방법
# B < A =< V
# (2,1,5)
# (5,1,6)
# (3,1,8)
# (100,99,10000000)
import sys
A,B,V=map(int, sys.stdin.readline().split())
ans=0
if (V-A) % (A-B) == 0:
    ans = (V-A)//(A-B) + 1
else:
    ans = (V-A)//(A-B) + 2
print(ans)
