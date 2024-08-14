n=int(input())
for i in range(n):
    add_score=0
    score=0
    for j in input():
        if j=="O":
            add_score+=1
            score+=add_score
        else:
            add_score=0
    print(score)