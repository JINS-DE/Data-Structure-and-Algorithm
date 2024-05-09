def solution(babbling):
    answer=0
    li=["aya", "ye", "woo", "ma"]
    for i in babbling:
        word=''
        before_word=''
        for j in i:
            word+=j
            if word in li:
                if before_word != word :
                    before_word=word
                    word=''
        if word=='':
            answer+=1
    return answer
# babbling 예시 
babbling=["ayayeayaye","mamama" "uuu", "yeye", "yemawoo", "ayay"]
print(solution(babbling))