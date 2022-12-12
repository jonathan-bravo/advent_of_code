from dataclasses import dataclass, field
from tqdm import tqdm

@dataclass
class Node():
    position: list[int] = field(default_factory=list)
    parent: object = None
    g: int = 0
    h: int = 0
    f: int = 0

    def __eq__(self, other):
        return self.position == other.position

    def possible_moves(self, maze, deltas):
        x, y = self.position[0], self.position[1]
        for dx, dy in deltas:
            newx, newy = x + dx, y + dy
            try:
                check = (
                    maze[newy][newx] <= (maze[y][x] + 1)
                    and newx >= 0
                    and newy >= 0
                )
                if check:
                    yield Node((newx, newy), self)
            except IndexError:
                pass


def astar(maze, start, end):
    deltas = (
        (1, 0), (-1, 0), # only x
        (0, 1), (0, -1) # only y
    )
    start_node = Node(start)
    end_node = Node(end)
    
    open_list = []
    closed_list = []
    
    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = sorted(open_list, key=lambda node: node.f)[0]
        current_index = open_list.index(current_node)

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        for neighbor in current_node.possible_moves(maze, deltas):
            old_f = neighbor.f
            if neighbor in closed_list:
                continue
            else:
                neighbor.g = current_node.g + 1
                neighbor.h = (end_node.position[0] - neighbor.position[0]) + (end_node.position[1] - neighbor.position[1])
                neighbor.f = neighbor.g + neighbor.h

            if neighbor not in open_list or neighbor.f < old_f: 
                open_list.append(neighbor)

def parse_matrix(matrix):
    parsed_matrix = []
    possible_starts = []
    for i,row in enumerate(matrix):
        parsed_row = []
        for j,val in enumerate(row):
            if val == 'S':
                start = (j,i)
                parsed_row.append(1)
                possible_starts.append(start)
            elif val == 'E':
                end = (j,i)
                parsed_row.append(26)
            else:
                parsed_row.append(ord(val) - 96)
                if (ord(val) - 96) == 1:
                    possible_starts.append((j,i))
        parsed_matrix.append(parsed_row)
    return parsed_matrix, possible_starts, start, end

def main():
    with open('12_input.txt') as f:
        matrix = [line.strip() for line in f]
        matrix = [[x for x in string] for string in matrix]
        maze, possible_starts, start, end = parse_matrix(matrix)
        path = astar(maze, start, end)
        new_paths = [astar(maze, s, end) for s in tqdm(possible_starts)]
        new_path = sorted([len(p) for p in new_paths if p is not None])[0]
        print(f'SILVER: {len(path)-1}')
        print(f'GOLD: {new_path-1}')

if __name__ == '__main__':
    main()


