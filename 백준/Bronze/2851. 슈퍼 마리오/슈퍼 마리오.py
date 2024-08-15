a=[int(input()) for _ in range(10)]
a_sum=0
for i in a:
    a_sum+=i
    if a_sum>=100:
        break
before_sum=a_sum-i

now_gap =abs(100-a_sum)
before_gap = abs(100-before_sum)

if now_gap == before_gap:
    print(a_sum)
elif now_gap > before_gap:
    print(before_sum)
else:       
    print(a_sum)