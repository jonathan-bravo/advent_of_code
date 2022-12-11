def gold(pair):
    pair = pair.strip().split(',')
    [a,b] = pair[0].split('-')
    [x,y] = pair[1].split('-')
    r1 = range(int(a),int(b)+1)
    r2 = range(int(x),int(y)+1)
    if set(r1).intersection(set(r2)) or set(r2).intersection(set(r1)):
        return 1
    else:
        return 0

def silver(pair):
    pair = pair.strip().split(',')
    [a,b] = pair[0].split('-')
    [x,y] = pair[1].split('-')
    r1 = range(int(a),int(b)+1)
    r2 = range(int(x),int(y)+1)
    if set(r1).issubset(set(r2)) or set(r2).issubset(set(r1)):
        return 1
    else:
        return 0

with open('4_input.txt') as f:
    pairs = f.readlines()
    num_overlaps_silver = sum(map(silver, pairs))
    print(num_overlaps_silver)
    num_overlaps_gold = sum(map(gold, pairs))
    print(num_overlaps_gold)
