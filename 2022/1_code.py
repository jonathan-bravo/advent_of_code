import pandas as pd

with open('1_input.txt') as f:
    count = 1
    total = 0
    df = pd.DataFrame(columns=['Elf', 'Calories'])
    for line in f:
        if line != '\n':
            total += int(line)
        else:
            df.loc[count-1] = [count, total]
            total = 0
            count += 1
    df.loc[count-1] = [count, total]
    top_elf = df.nlargest(1, ['Calories']).to_string(index=False)
    print(f'The elf with the most calories is:\n\n{top_elf}')
    top_three = df.nlargest(3, ['Calories']).to_string(index=False)
    print(f'The top three elves are:\n\n{top_three}')
    top_three_sum = df.nlargest(3, ['Calories']).sum()
    top_three_cals = top_three_sum['Calories']
    print(f'Total cals of top three: {top_three_cals}')
