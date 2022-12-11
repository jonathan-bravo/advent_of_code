def simulate(val, metal):
    val_dict = {'A':0, 'X':0, 'B':1, 'Y':1, 'C':2, 'Z':2}
    them = val_dict[val[0]]
    me = val_dict[val[2]]
    if metal == 'SILVER':
        if me == them: score = me + 4
        elif (me-them)%3 == 1: score = me + 7
        elif (me-them)%3 == 2: score = me + 1
    elif metal == 'GOLD':
        gold = {0: ((them - 1) % 3) + 1,
                1: them + 4,
                2: ((them + 1) % 3) + 7}
        score = gold[me]
    return score
 
def main():
    with open('2_input.txt') as f:
        data = f.readlines()
    silver = sum([simulate(val, 'SILVER') for val in data])
    gold = sum([simulate(val, 'GOLD') for val in data])
    print(f'SILVER: {silver}')
    print(f'GOLD: {gold}')

if __name__ == '__main__':
    main()