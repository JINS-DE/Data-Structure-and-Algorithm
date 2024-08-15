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

real_row_li=[]
real_col_li=[]
value = 0
for row in row_li:
    real_row_li.append(row-value)
    value = row
value = 0
for col in col_li:
    real_col_li.append(col-value)
    value = col

print(max(real_row_li)*max(real_col_li))