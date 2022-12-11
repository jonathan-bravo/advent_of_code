def crt(cycle, x):
    position = (cycle - 1) % 40
    if position in range(x-1, x+2):
        draw = '#'
    else:
        draw = '.'
    if cycle % 40 == 0:
        print(draw)
    else:
        print(draw, end='')

def main():
    with open('10_input.txt') as f:
        x = 1
        cycle = 1
        cycle_checks = (20, 60, 100, 140, 180, 220)
        signals = []
        results = []
        for line in f:
            if 'noop' in line.strip():
                crt(cycle, x)
                signals.append((cycle, x))
                cycle += 1
            else:
                crt(cycle, x)
                signals.append((cycle, x))
                cycle += 1
                crt(cycle, x)
                signals.append((cycle, x))
                cycle += 1
                x += int(line.strip().split(' ')[1])
        for signal in signals:
            if signal[0] in cycle_checks:
                results.append(signal[0]*signal[1])
        print(f'SILVER: {sum(results)}')


if __name__ == '__main__':
    main()