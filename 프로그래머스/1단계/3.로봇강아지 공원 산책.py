park=["OSO","OOO","OXO","OOO"]
routes =["E 2","S 3","W 1"]
w = len(park[0])-1 #가로
h = len(park)-1 #세로

cnt = 0
for i in park:
    if 'S' in i:
        x,y = cnt,i.find("S")
    cnt+=1
print(x,y)
for i in routes:
    xx=x
    yy=y
    for j in range(int(i[-1])):

        if i[0] =='E' and yy!=w and park[xx][yy+1] != 'X' :
            yy+=1
            if j == int(i[-1])-1:
                y=yy
        elif i[0] =='W' and yy!=0 and park[xx][yy-1] != 'X' :
            yy-=1
            if j == int(i[-1])-1:
                y=yy
        elif i[0] =='N' and xx!=0 and park[xx-1][yy] != 'X' :
            xx-=1
            if j == int(i[-1])-1:
                x=xx
        elif i[0] =='S' and xx!=h and park[xx+1][yy] != 'X' :
            xx+=1
            if j == int(i[-1])-1:
                x=xx



print(x,y)
        