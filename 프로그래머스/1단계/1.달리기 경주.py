players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

# #test
# # 1번 
# player_dict = {player:rank for rank, player in enumerate(players)}
# rank_dict = {rank:player for rank, player in enumerate(players)}
# print(player_dict,"\n",rank_dict)

# for i in callings:
#     rank = player_dict[i]
#     player_dict[rank_dict[rank]], player_dict[rank_dict[rank-1]] = player_dict[rank_dict[rank-1]], player_dict[rank_dict[rank]]
#     rank_dict[rank-1], rank_dict[rank] = rank_dict[rank], rank_dict[rank-1]

# # 2번
# players_dict = {player : rank for rank, player in enumerate(players)}
# rank_dict = {rank : player for rank,player in enumerate(players)}

# for i in callings:
#     called_rank = players_dict[i]
#     players_dict[i] -= 1
#     players_dict[rank_dict[called_rank-1]] += 1
#     rank_dict[called_rank-1], rank_dict[called_rank] = rank_dict[called_rank], rank_dict[called_rank-1]





