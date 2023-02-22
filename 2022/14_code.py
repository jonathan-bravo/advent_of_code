# input is the vectors that make the rock walls
## each line is a wall and wach vector is a line that is part of that wall

# could make a class for the sand? Although that doesn't seem like it's worth
## it unless I am tracking relation to other sand units

# first try was 884 and that was too low
# seconds guess? 1298

from time import sleep

def rock_path(vectors):
    path = [()]
    for i in range(len(vectors)-1):
        path.pop()
        start = [int(x) for x in vectors[i].split(',')]
        stop = [int(y) for y in vectors[i+1].split(',')]
        diff = [a-b for a,b in zip(stop, start)]
        if diff[0] == 0 and diff[1] > 0:
            for y in range(start[1], stop[1]+1):
                path.append((start[0], y))
        elif diff[0] == 0 and diff[1] < 0:
            for y in range(start[1], stop[1]-1, -1):
                path.append((start[0], y))
        elif diff[1] == 0 and diff[0] > 0:
            for x in range(start[0], stop[0]+1):
                path.append((x, start[1]))
        elif diff[1] ==0 and diff[0] < 0:
            for x in range(start[0], stop[0]-1, -1):
                path.append((x, start[1]))
    return path

# def find_floor(rock_paths):
#     return max([y for x,y in rock_paths]) + 2

def sand(rock_paths, sand_units):
    position = [500,0]
    stop = False
    count = 0
    while not stop and count < 1000:
        neighbors = {'down':(position[0], position[1] + 1), 'left': (position[0] - 1, position[1] + 1), 'right': (position[0] + 1, position[1] + 1)}
        if neighbors['down'] in rock_paths or neighbors['down'] in sand_units:
            if neighbors['left'] in rock_paths or neighbors['left'] in sand_units:
                if neighbors['right'] in rock_paths or neighbors['right'] in sand_units:
                    stop = True
                else:
                    position[0] += 1
                    position[1] += 1
                    count = 0
            else:
                position[0] -= 1
                position[1] += 1
                count = 0
        else:
            position[1] += 1
            count += 1
    if count >= 1000: position = [-1,-1]
    return tuple(position)

def main():
    rock_paths = []
    silver_sand_units = []
    gold_sand_units = []
    with open('14_input.txt') as f:
        for line in f:
            [rock_paths.append(path) for path in rock_path(line.strip().split(' -> '))]
    
    # PART 1
    # while (-1,-1) not in silver_sand_units:
    #     silver_sand_units.append(sand(rock_paths, silver_sand_units))
    # print(len(silver_sand_units)-1)

    # PART 2
    floor = max([y for x,y in rock_paths]) + 2
    #print(floor)
    [rock_paths.append((i, floor)) for i in range(-10000, 10001)]
    # print(max([x for x,y in rock_paths]))
    # print(min([x for x,y in rock_paths]))
    while (500,0) not in gold_sand_units:
        # print(gold_sand_units, end='\r', flush=True)
        # sleep(0.5)
        gold_sand_units.append(sand(rock_paths, gold_sand_units))
    #print(gold_sand_units)
    print(len(gold_sand_units))


if __name__ == '__main__':
    main()