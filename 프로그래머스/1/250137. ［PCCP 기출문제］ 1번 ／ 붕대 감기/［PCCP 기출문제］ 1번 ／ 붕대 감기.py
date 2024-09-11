def solution(bandage, health, attacks):
    hp=health
    b_a = 0 # before monster attack time
    for i in attacks:
        time_diff=i[0]-b_a-1 
        hp+=(time_diff//bandage[0])*bandage[2] + bandage[1]*time_diff
        if hp>=health:
            hp=health
        hp-=i[1]
        
        if hp<=0:
            return -1
        
        b_a=i[0] 
    return hp