def solution(rny_string):
    answer = ''
    for st in rny_string:
        answer+=st if st!="m" else "rn"
        
    return answer