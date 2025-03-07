import math
from collections import defaultdict
def solution(fees, records):
    basic_time,basic_fee, per_time, per_fee =fees
    in_list=[]
    out_list=[]
    time_dic=defaultdict(int)
    for record in records:
        time, number, inout = record.split()
        h,m=map(int,time.split(':'))
        time=h*60+m
        if inout=='IN':
            in_list.append((number,time))
        else:
            out_list.append((number,time))
    
    in_list.sort(reverse=True)
    out_list.sort(reverse=True)

    while in_list:
        in_num, in_time = in_list.pop()
        if out_list:
            out_num, out_time = out_list.pop()
        else:
            out_num=None
        
        if in_num==out_num:
            total_time = out_time-in_time
            time_dic[in_num]+=total_time
        
        else:
            total_time = (23*60+59)-in_time
            time_dic[in_num]+=total_time
            if out_num != None:
                out_list.append((out_num,out_time))
                
    answer=[]
    li = list(time_dic.keys())
    li.sort()
    for number in li:
        t=time_dic[number]
        print(t)
        if t <= basic_time:
            answer.append(basic_fee)
        else:
            answer.append(basic_fee + math.ceil((t-basic_time)/per_time)*per_fee)
            
        

            
    return answer