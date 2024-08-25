'''
해결방안
* '-'가 나오면 뒤에 숫자들의 합을 구하고 -를 해줌
'''
import re
st=input()
minus_index=st.find('-')
if minus_index!=-1:
    print(sum(map(int,re.split(r'[+]',st[:minus_index])))-sum(map(int,re.split(r'[+-]',st[minus_index+1:]))))
else:
    print(sum(map(int,re.split(r'[+]',st))))