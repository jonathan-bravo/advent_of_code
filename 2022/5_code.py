from copy import deepcopy

def parse_crate_positions(crate_data):
    crates = {}
    columns = crate_data[-1].strip().split()
    for column in columns: crates[int(column)] = []
    for stack in crate_data[:-1]:
        stack = stack.strip('\n')
        for i, char_col in enumerate(stack):
            if char_col == '[':
                crates[int(i/4)+1].append(stack[i+1])
    for column in crates: crates[column] = crates[column][::-1]
    return crates


def process_crates_silver(crates, proc):
    for command in proc:
        # number of crates to move [1], from col [3], to col [5]
        command = command.strip().split(' ')
        num_crates = int(command[1])
        from_col = int(command[3])
        to_col = int(command[5])
        for _ in range(num_crates):
            crates[to_col].append(crates[from_col].pop())
    return crates


def process_crates_gold(crates, proc):
    for command in proc:
        # number of crates to move [1], from col [3], to col [5]
        command = command.strip().split(' ')
        num_crates = int(command[1])
        from_col = int(command[3])
        to_col = int(command[5])
        crates[to_col].extend(crates[from_col][-num_crates:])
        crates[from_col] = crates[from_col][:-num_crates]
    return crates


def list_caps(crates):
    caps = []
    for i in range(len(crates)):
        caps.append(crates[i+1][-1])
    print(''.join(caps))


with open('5_input.txt') as f:
    crate_data = []
    proc = []
    crate_info = True
    for line in f:
        if line == '\n': crate_info = False
        if crate_info:
            crate_data.append(line)
        else:
            proc.append(line)
    proc = proc[1:]
    crates = parse_crate_positions(crate_data)
    crates_1 = deepcopy(crates)
    crates_2 = deepcopy(crates)
    silver_crates = process_crates_silver(crates_1, proc)
    list_caps(silver_crates)
    gold_crates = process_crates_gold(crates_2, proc)
    list_caps(gold_crates)