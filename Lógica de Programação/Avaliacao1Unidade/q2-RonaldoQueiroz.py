def determine_group(game_results):
    wins = game_results.count('V')
    
    if wins >= 5:
        return 1
    elif 3 <= wins <= 4:
        return 2
    elif 1 <= wins <= 2:
        return 3
    else:
        return -1

game_results = [input() for _ in range(6)]
print(determine_group(game_results))
