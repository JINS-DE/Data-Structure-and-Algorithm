def solution(myString):
    answer=''
    for st in myString:
        if 'A'<=st<='Z':
            answer+=chr(ord(st)+32)
        else:
            answer+=st
    return answer