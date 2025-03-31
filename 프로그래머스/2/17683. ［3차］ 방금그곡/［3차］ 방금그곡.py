def change_melody(st):
    for i in range(7):
        st = st.replace(chr(65 + i) + '#', chr(65 + i + 7))
    return st

def solution(m, musicinfos):
    answer_li = []
    answer = ''
    m = change_melody(m)
    
    candidate = []
    for music in musicinfos:
        start, end, title, melody = music.split(',')
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])
        play_time = end - start
        melody = change_melody(melody)
    
        n = len(melody)
        
        melody = melody * (play_time // n) + melody[:(play_time % n)]
        candidate.append([melody, title])
    
    for candi in candidate:
        if m in candi[0]:
            answer_li.append(candi)
    
    if answer_li:
        answer_li.sort(key=lambda x: (-len(x[0]), x[1]))  
    else:
        return "(None)"
    
    return answer_li[0][1]
