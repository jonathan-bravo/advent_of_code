def simulate(pair, metal): # gold
    pair = pair.strip().split(',')
    [a,b] = pair[0].split('-')
    [x,y] = pair[1].split('-')
    r1 = range(int(a),int(b)+1)
    r2 = range(int(x),int(y)+1)
    cases = {
        'SILVER': set(r1).issubset(set(r2)) or set(r2).issubset(set(r1)),
        'GOLD': set(r1).intersection(set(r2)) or set(r2).intersection(set(r1))}
    if cases[metal]:
        return 1
    else:
        return 0

def main():
    with open('4_input.txt') as f:
        pairs = f.readlines()
        silver = sum([simulate(pair, 'SILVER') for pair in pairs])
        gold = sum([simulate(pair, 'GOLD') for pair in pairs])
        print(f'SILVER: {silver}')
        print(f'GOLD: {gold}')

if __name__ == '__main__':
    main()