from math import copysign

def update_head(head, m):
    move_dict = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
    return [x + y for (x, y) in zip(head, move_dict[m])]

def update_tail(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    if abs(dx) <= 1 and abs(dy) <= 1: # escapes all combos of 0 and 1 for x,y
        return tail
    if abs(dx) >= 1: # captures all left/right
        tail[0] += int(copysign(1, dx))
    if abs(dy) >= 1: # captures all up/down
        tail[1] += int(copysign(1, dy))
    
    return tail

def simulate(data, rope_length):
    rope = [[0,0]] * rope_length
    tail_loc = []
    for m,n in data:
        for _ in range(n):
            rope[0] = update_head(rope[0], m)
            for t in range(1, len(rope)):
                rope[t] = update_tail(rope[t-1].copy(), rope[t].copy())
            tail_loc.append(tuple(rope[-1]))
    return len(set(tail_loc))

def main():
    with open('9_input.txt') as f:
        data = [line.strip() for line in f]

    data = [[r.split()[0], int(r.split()[1])] for r in data]

    silver = simulate(data, 2)
    gold = simulate(data, 10)

    print(f'SILVER: {silver}')
    print(f'GOLD: {gold}')


if __name__ == '__main__':
    main()