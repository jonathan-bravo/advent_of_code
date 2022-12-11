## MY FIRST TRY

# with open('7_input.txt') as f:
#     file_layout = f.readlines()
#     flat_map = ' '.join(file_layout).split('$')[1:]
#     files = {}
#     pointer = ''
#     for line in flat_map:
#         entries = line.split('\n')
#         if entries[0] == ' ls':
#             files[pointer].extend(entries[1:])
#             files[pointer] = [x for x in files[pointer] if 'dir' not in x]
#             files[pointer] = [x.split(' ')[1] for x in files[pointer]]
#         if ' cd' in entries[0]:
#             if entries[0][-1] == '.':
#                 pointer = pointer[:-2]
#             else:
#                 pointer = pointer + entries[0].split()[-1] + '-'
#                 files[pointer] = []
#     paths = [n.split('-')[:-1] for n in files.keys() if '/' in n]

#     flat_paths = list(set([item for sublist in paths for item in sublist]))

#     sizes_to_add = []

#     for p in flat_paths:
#         size_total = 0
#         for key in files.keys():
#             if p in key:
#                 for value in files[key]:
#                     if value != '':
#                         size_total += int(value)
#         print(p, size_total)
#         if size_total <= 100000:
#             #print(p, size_total)
#             sizes_to_add.append(size_total)

#     #print(sum(sizes_to_add))





SIZE_VALUES = []

def parse_lines(f):
    total = 0
    while len(f) > 0:
        line = f.pop(0)
        if line[0] == '$' and 'cd' in line and '..' not in line:
            total += parse_lines(f)
        elif 'dir ' not in line and '$' not in line:
            total += int(line.split(' ')[0])
        elif '$ cd ..' in line:
            SIZE_VALUES.append(total)
            return total
    return total


with open('7_input.txt') as f:
    TOTAL_DISK = 70000000
    UPDATE_SPACE = 30000000
    file_data = f.readlines()
    test_list = []
    root_value = parse_lines(file_data)
    space_needed = UPDATE_SPACE - (TOTAL_DISK - root_value)
    silver_values = [x for x in SIZE_VALUES if x <= 100000]
    gold_values = [x for x in SIZE_VALUES if x >= space_needed]
    print(f'SILVER: {sum(silver_values)}')
    print(f'Space Needed: {space_needed}')
    print(f'Gold value: {sorted(gold_values)[0]}')












## MY ATTEMPT AT RECURSION


# def process_dir(to_process):
#     print(to_process)
#     current_size = 0
#     size_values = []
#     while len(to_process) != 0:
#         if to_process[-1] == 'cd':
#             size_values.append(current_size)
#             to_process.pop()
#         else:
#             current_size += to_process.pop()
#     return size_values

# with open('7_input.txt') as f:
#     next(f)
#     size_values = []
#     to_process = []
#     for line in f:
#         if line[0] == '$' and 'cd' in line and '..' not in line:
#             to_process.append('cd')
#             #print(to_process)
#         elif 'dir ' not in line and '$' not in line:
#             to_process.append(int(line.split(' ')[0]))
#             #print(to_process)
#         elif line[0] == '$' and 'cd ..' in line:
#             size_values.append(process_dir(to_process))
#             to_process = []
#             #print(to_process)
#     size_values.append(process_dir(to_process))
#     all_sizes = [item for sublist in size_values for item in sublist]
#     correct_size_vals = [item for sublist in size_values for item in sublist if item <= 100000]
#     print(sum(all_sizes))
#     #print(size_values)
#     print(sum(correct_size_vals))