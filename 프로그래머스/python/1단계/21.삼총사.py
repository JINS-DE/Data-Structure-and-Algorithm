number=	[-3, -2, -1, 0, 1, 2, 3]

answer = 0
for i in range(len(number)-2):
    for j in range(i+1,len(number)-1):
        for k in range(j+1,len(number)):
            if number[i]+number[j]+number[k] == 0:
                answer+=1
print(answer)