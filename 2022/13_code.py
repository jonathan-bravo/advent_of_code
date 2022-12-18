def com_pair(left, right):
    compare = list(zip(left, right))

    while len(compare) > 0:
        l, r = compare.pop(0)

        if type(l) == list and type(r) == list:
            result = com_pair(l, r)
            if type(result) == bool: return result
            else: continue

        elif type(l) == list and type(r) == int:
            result = com_pair(l, [r])
            if type(result) == bool: return result
            else: continue

        elif type(l) == int and type(r) == list:
            result = com_pair([l], r)
            if type(result) == bool: return result
            else: continue

        elif type(l) == int and type(r) == int:
            if l < r:  return True
            elif l > r: return False

    if len(left) < len(right): return True
    elif len(left) > len(right): return False
    else: return None

def sort(l):
    quicksort(l, 0, len(l) - 1)
    return l

def quicksort(l, head, tail):
    if head < tail:
        pivot = partition(l, head, tail)
        quicksort(l, head, pivot - 1)
        quicksort(l, pivot + 1, tail)

def partition(l, head, tail):
    pivot = l[tail]
    n = head
    for i in range(head, tail):
        if com_pair(eval(l[i]), eval(pivot)):
            l[i], l[n] = l[n], l[i]
            n = n + 1
    l[n], l[tail] = l[tail], l[n]		
    return n

def main():
    with open('13_input.txt') as f:
        data = [line.strip() for line in f]
        
    # PART 1
    left = data[::3]
    right = data[1::3]

    correct = []
    for i, pair in enumerate(zip(left, right)):
        correct.append(com_pair(eval(pair[0]), eval(pair[1])))
    
    silver = 0
    for i, x in enumerate(correct):
        if x:
            silver += i+1

    print(silver)

    # PART 2
    all_signals = [x for x in data if x != '']
    all_signals.append('[[2]]')
    all_signals.append('[[6]]')
    sort(all_signals)
    gold = (all_signals.index('[[2]]')+1) * (all_signals.index('[[6]]')+1)
    print(gold)

if __name__ == '__main__':
    main()