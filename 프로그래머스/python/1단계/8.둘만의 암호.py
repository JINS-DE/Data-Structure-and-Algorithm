s="aukks"
skip="wbqd"


index = 5

result=""

# for i in s:
#     cnt=0
#     for j in skip:
#         if ord(i)<ord(j) and ord(j) <= ord(i)+index:
#             cnt+=1
#     chr_n = ord(i)+index+cnt
#     if chr_n > 122:
#         chr_n=ord('a')+chr_n%122-1
#     result+=chr(chr_n)
# print(result)



# 정답 
abc = [chr(i) for i in range(97, 123) if not chr(i) in skip]
answer = ''
for i in s:
    answer += abc[(abc.index(i) + index)%len(abc)]
print(answer)
