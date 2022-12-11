from dataclasses import dataclass, field
from numpy import prod

@dataclass
class Monkey:
    items:list[list] = field(default_factory=list)
    operation:str = ''
    test:int = 0
    t_case:str = ''
    f_case:str = ''
    inspect_count:int = 0

    def do_round(self, m_dict, metal, lcm):
        for old in self.items:
            cases = {'SILVER': eval(self.operation) // 3,
                     'GOLD': int(eval(self.operation) % lcm)}
            new = cases[metal]
            send_to = {True: m_dict[self.t_case].items,
                       False: m_dict[self.f_case].items}
            send_to[new % self.test == 0].append(new)
            self.inspect_count += 1
        self.items = []

def make_monkeys(monkeys):
    m_dict = {}
    for m in monkeys:
        m_dict[m[0][:-1].lower()] = Monkey(
            [int(item) for item in m[1].split(':')[1].strip(' ').split(', ')],
            m[2].split(' = ')[1],
            int(m[3].split(' ')[-1]),
            ' '.join(m[4].split(' ')[-2:]),
            ' '.join(m[5].split(' ')[-2:])
        )
    return m_dict

def simulate(monkeys, metal, rounds):
    m_dict = make_monkeys(monkeys)
    lcm = prod([m_dict[m].test for m in m_dict])
    for _ in range(rounds):
        for m in m_dict:
            m_dict[m].do_round(m_dict, metal, lcm)
    m_business = prod(sorted([m_dict[m].inspect_count for m in m_dict])[-2:])
    print(f'{metal}: {m_business}')
    
def main():
    cases = {'SILVER': 20, 'GOLD': 10000}
    with open('11_input.txt') as f:
        data = [line.strip() for line in f if line.strip() != '']
    monkeys = [data[x:x+6] for x in range(0, len(data), 6)]
    for case in cases:
        simulate(monkeys, case, cases[case])

if __name__ == '__main__':
    main()