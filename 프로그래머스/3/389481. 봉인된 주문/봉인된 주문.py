def alpa_to_digit(s):
    digit=0
    # print(s)
    s=s[::-1]
    for i,v in enumerate(s):
        digit+=(ord(v)-96)*(26**i)
    return digit

def digit_to_alpa(n):
    st=''
    stack=[]
    while n>0:
        stack.append(chr((n-1)%26 + 97))
        n = (n-1) // 26

    return ''.join(stack[::-1])

def solution(n, bans):
    bans.sort(key=lambda s: (len(s), s))
    for ban in bans:
        num = alpa_to_digit(ban)
        if num <= n:
            n+=1
        else:
            break
    
    return digit_to_alpa(n)