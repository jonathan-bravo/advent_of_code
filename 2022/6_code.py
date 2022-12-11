
def parse_data(data_stream, x):
    data_parts = [(data_stream[0][i-x:i], i) for i in range(x,len(data_stream[0]))]

    for parts in data_parts:
        if len(set(parts[0])) == x:
            print(f'{parts[1]} {parts[0]}')
            break

with open('6_input.txt') as f:
    data_stream = f.readlines()
    silver = 4
    gold = 14
    parse_data(data_stream, silver)
    parse_data(data_stream, gold)
