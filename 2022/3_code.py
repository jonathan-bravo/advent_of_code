def get_item_priority_gold(group):
    shared_item = list(
        set(group[2].strip()).intersection(
            set(group[0].strip()).intersection(
                group[1].strip()
            )
        )
    )[0]
    if shared_item.isupper():
        item_priority = ord(shared_item) - 38
    else:
        item_priority = ord(shared_item) - 96
    return item_priority

def get_item_priority_silver(rucksack):
    rucksack = rucksack.strip()
    items = int(len(rucksack)/2)
    shared_item = list(set(rucksack[:items]).intersection(rucksack[items:]))[0]
    if shared_item.isupper():
        item_priority = ord(shared_item) - 38
    else:
        item_priority = ord(shared_item) - 96
    return item_priority

with open('3_input.txt') as f:
    rucksacks = f.readlines()
    groups = [list(rucksacks[i:i+3]) for i in range(0,len(rucksacks),3)]
    item_priority_sum_gold = sum(map(get_item_priority_gold, groups))
    item_priority_sum_silver = sum(map(get_item_priority_silver, rucksacks))
    print(item_priority_sum_silver)
    print(item_priority_sum_gold)