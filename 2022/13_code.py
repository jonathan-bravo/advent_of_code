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






# def flatten(container):
#     for i in container:
#         if isinstance(i, list):
#             for j in flatten(i):
#                 yield j
#         else:
#             yield i

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
    left.append()

if __name__ == '__main__':
    main()



