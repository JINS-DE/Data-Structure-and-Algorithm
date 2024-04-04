keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
answer = []


# for i in targets:
#     for j in i:
        


def test(target):
    li=[]
    for i in keymap:
        li.append(i.find(target))
    
    if min(li) >= 0 :
        return min(li)+1
    else:
        if max(li)==-1:
            return -1
        else:
            return min(filter(lambda x: x>-1 , li))+1




for i in targets:
    cnt=0
    for j in i:
        if test(j)==-1:
            cnt=-1
            break
        cnt+=test(j)
    answer.append(cnt)

print(answer)




# 남이 한거

# def solution(keymap, targets):
#     answer = []
#     hs = {}
#     for k in keymap:
#         for i, ch in enumerate(k):
#             hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

#     for i, t in enumerate(targets):
#         ret = 0
#         for ch in t:
#             if ch not in hs:
#                 ret = - 1
#                 break
#             ret += hs[ch]
#         answer.append(ret)

#     return answer



