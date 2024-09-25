def solution(players, callings):    
    player_dict = {player:rank for rank, player in enumerate(players)}
    rank_dict = {rank:player for rank, player in enumerate(players)}
    
    for i in callings:
        called_rank = player_dict[i]
        player_dict[i] -= 1
        player_dict[rank_dict[called_rank-1]] += 1
        rank_dict[called_rank-1], rank_dict[called_rank] = rank_dict[called_rank], rank_dict[called_rank-1]

    return list(rank_dict.values())