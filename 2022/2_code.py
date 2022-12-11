def parse_round_gold(val):
    val_dict = {'A':0, 'B':1, 'C':2}
    them = val_dict[val[0]]
    me = val[2]
    if me == 'Y':
        score = them + 4
    elif me == 'Z':
        score = ((them + 1) % 3) + 7
    elif me == 'X':    
        score = ((them - 1) % 3) + 1
    return score


def parse_round_silver(val):
    val_dict = {'A':1, 'X':1, 'B':2, 'Y':2, 'C':3, 'Z':3}
    them = val_dict[val[0]]
    me = val_dict[val[2]]
    if me == them:
        score = me + 3
    elif (me-them)%3 == 1:
        score = me + 6
    elif (me-them)%3 == 2:
        score = me
    return score
    

with open('2_input.txt') as f:
    vals = f.readlines()
    total_score_silver = sum(map(parse_round_silver, vals))
    total_score_gold = sum(map(parse_round_gold, vals))
    print(total_score_silver)
    print(total_score_gold)