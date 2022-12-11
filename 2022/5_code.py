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

def process_crates(crates, proc, metal):
    for command in proc:
        command = command.strip().split(' ')
        num_crates = int(command[1])
        from_col = int(command[3])
        to_col = int(command[5])
        if metal == 'SILVER':
            for _ in range(num_crates):
                crates[to_col].append(crates[from_col].pop())
        elif metal == 'GOLD':
            crates[to_col].extend(crates[from_col][-num_crates:])
            crates[from_col] = crates[from_col][:-num_crates]
    return crates

def list_caps(crates, metal):
    caps = []
    for i in range(len(crates)):
        caps.append(crates[i+1][-1])
    print(f"{metal}: {''.join(caps)}")

def parse_input(f):
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
    return crate_data, proc

def main():
    cases = ('SILVER', 'GOLD')
    with open('5_input.txt') as f:
        crate_data, proc = parse_input(f)
    crates = parse_crate_positions(crate_data)
    for metal in cases:
        metal_crates = process_crates(deepcopy(crates), proc, metal)
        list_caps(metal_crates, metal)

if __name__ == '__main__':
    main()