'''
10 8 : 종이 가로 세로
3 : 칼로 잘라야 하는 점섬의 개수
0 3 : 가로 3번
1 4 : 세로 4번
0 2 : 가로 2번
'''

row_length,col_length=map(int,input().split())
row_li = [col_length]
col_li = [row_length]
for i in range(int(input())):
    type_, loc =map(int,input().split())
    if type_==0:
        row_li.append(loc)
    else:
        col_li.append(loc)

row_li=sorted(row_li)
col_li=sorted(col_li)

row_length_list=[]
col_length_list=[]
value = 0
for row in row_li:
    row_length_list.append(row-value)
    value = row
value = 0
for col in col_li:
    col_length_list.append(col-value)
    value = col

print(max(row_length_list)*max(col_length_list))



