wallpaper =  ["..........", ".....#....", "......##..", "...##.....", "....#....."]

a,b =[],[]

for i in range(len(wallpaper)):
    for j in range(len(wallpaper[i])):
        if wallpaper[i][j]=='#':
            a.append(i)
            b.append(j)
    
print(min(a),min(b),max(a)+1,max(b)+1)


# 어렵게 풀고 딜레이 오류걸림.. ㅠㅠ
# min_x=min(map(lambda x: x.find('#') if x.find('#') != -1 else len(x)+1, wallpaper ))
# max_x=max(map(lambda x: x.rfind('#'),wallpaper))


# min_y=0
# for i in wallpaper:
#     if '#' in i:
#         break
#     min_y+=1


# for i in range(-1,-len(wallpaper),-1):
#     if '#' in wallpaper[i]:
#         break
# max_y=len(wallpaper)+i


# print(min_y,min_x,max_y+1,max_x+1)