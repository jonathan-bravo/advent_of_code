def main():
    with open('1_input.txt') as f:
        data = ','.join([line.strip() for line in f]).split(',,')
        data = [x.split(',') for x in data]
        f = lambda x: sum([int(cal) for cal in x])
        results = sorted([f(x) for x in data])
        print(f'SILVER: {results[-1]}')
        print(f'GOLD: {sum(results[-3:])}')

if __name__ == '__main__':
    main()