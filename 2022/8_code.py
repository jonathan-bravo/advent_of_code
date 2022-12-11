import numpy as np


def get_matrix(filename):
    with open(filename) as f:
        trees = []
        for line in f:
            trees.append([*line.strip()])
    return np.matrix(trees)


def get_range(direction, row, col, row_shape, col_shape):
    if direction == 'up':
        return reversed(range(0, row))
    elif direction == 'down':
        return range(row+1, row_shape)
    elif direction == 'left':
        return reversed(range(0, col))
    elif direction == 'right':
        return range(col+1, col_shape)


def neighbor_value(direction, position, tree_matrix, row, col):
    if direction == 'up' or direction == 'down':
        return tree_matrix[position, col]
    elif direction == 'left' or direction == 'right':
        return tree_matrix[row, position]

# only used in SILVER
def viewable(direction, tree_matrix, row, col, space):
    self_val = tree_matrix[row, col]
    for position in space:
        neighbor_val = neighbor_value(direction, position, tree_matrix, row, col)
        if neighbor_val >= self_val:
            return False
    return True


def silver(DIRECTIONS, tree_matrix, shape, row, col, on_border):
    if on_border:
        return True
    else:
        for direction in DIRECTIONS:
            space = get_range(direction, row, col, shape[0], shape[1])
            is_viewable = viewable(direction, tree_matrix, row, col, space)
            if is_viewable:
                return is_viewable
        return False


def scenic_score(direction, tree_matrix, row, col, space):
    self_val = tree_matrix[row, col]
    score = 0
    for position in space:
        # print(position)
        neighbor_val = neighbor_value(direction, position, tree_matrix, row, col)
        if neighbor_val >= self_val:
            score += 1
            break
        else:
            score += 1
    return score


def gold(DIRECTIONS, tree_matrix, shape, row, col, on_border):
    if not on_border:
        scores = []
        for direction in DIRECTIONS:
            space = get_range(direction, row, col, shape[0], shape[1])
            score = scenic_score(direction, tree_matrix, row, col, space)
            scores.append(score)
        # print(f'{scores}  ({row}, {col})  {tree_matrix[row, col]}')
        return np.prod(scores)
    return 0


def main():
    DIRECTIONS = ('up', 'left', 'right', 'down')

    tree_matrix = get_matrix('8_input.txt')
    shape = np.shape(tree_matrix)

    it = np.nditer(tree_matrix, flags=['multi_index'])

    silver_count = 0
    gold_list = []

    # print(tree_matrix)

    for _ in it:
        row = it.multi_index[0]
        col = it.multi_index[1]
        on_border = (
            row == 0 or row == shape[0]-1
            or col == 0 or col == shape[1]-1
        ) 
        
        # for SILVER
        is_viewable = silver(DIRECTIONS, tree_matrix, shape, row, col, on_border)
        if is_viewable:
            silver_count += 1

        # for GOLD
        score = gold(DIRECTIONS, tree_matrix, shape, row, col, on_border)
        gold_list.append(score)
    
    gold_result = sorted(gold_list)[-1]
    # print(tree_matrix[1,2])
    # print(tree_matrix[1,3])
    # print(tree_matrix[1,4])
    print(f'SILVER: {silver_count}')
    print(f'GOLD: {gold_result}')


if __name__ == '__main__':
    main()