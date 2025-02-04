def time_to_second(time):
    m,s = map(int,time.split(':'))
    return m*60+s

def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = time_to_second(video_len)
    pos_sec = time_to_second(pos)
    op_start_sec = time_to_second(op_start)
    op_end_sec = time_to_second(op_end)
    if op_start_sec <= pos_sec <=op_end_sec:
        pos_sec = op_end_sec

    for command in commands:
        if command == "next":
            pos_sec+=10
        else:
            pos_sec-=10
        
        if pos_sec < 0:
            pos_sec=0
        elif pos_sec > video_len_sec:
            pos_sec = video_len_sec
        
        if op_start_sec<=pos_sec<=op_end_sec:
            pos_sec = op_end_sec

    pos_m,pos_s = pos_sec//60, pos_sec%60
    if pos_m < 10:
        pos_m="0"+str(pos_m)
    if pos_s <10:
        pos_s="0"+str(pos_s)
    answer = f'{pos_m}:{pos_s}'
    
    return answer