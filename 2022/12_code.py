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
                valid = ( maze[newy][newx] <= (maze[y][x] + 1)
                          and newx >= 0
                          and newy >= 0 )
                if valid:
                    yield Node((newx, newy), self)
            except IndexError:
                pass

    def give_path(self):
        path = []
        current = self
        while current is not None:
            path.append(current.position)
            current = current.parent
        return path[::-1]

def astar(maze, start, end):
    deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))
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
            return current_node.give_path()

        for neighbor in current_node.possible_moves(maze, deltas):
            old_f = neighbor.f

            if neighbor not in closed_list:
                neighbor.g = current_node.g + 1
                neighbor.h = sum([x-y for (x,y) in zip(end_node.position, neighbor.position)])
                neighbor.f = neighbor.g + neighbor.h

                if neighbor not in open_list or neighbor.f < old_f:
                    open_list.append(neighbor)

def main():
    with open('12_input.txt') as f:
        matrix = [line.strip() for line in f]
        matrix = [[ord(x)-96 for x in string] for string in matrix]
        [start] = [(index2,index1) for (index1,sub_list) in enumerate(matrix) for (index2,element) in enumerate(sub_list) if element==-13]
        matrix[start[1]][start[0]] = 1
        [end] = [(index2,index1) for (index1,sub_list) in enumerate(matrix) for (index2,element) in enumerate(sub_list) if element==-27]
        matrix[end[1]][end[0]] = 26
        possible_starts = [(index2,index1) for (index1,sub_list) in enumerate(matrix) for (index2,element) in enumerate(sub_list) if element==1]
        path = astar(matrix, start, end)
        new_paths = [astar(matrix, s, end) for s in tqdm(possible_starts)]
        new_path = sorted([len(p) for p in new_paths if p is not None])[0]
        print(f'SILVER: {len(path)-1}')
        print(f'GOLD: {new_path-1}')

if __name__ == '__main__':
    main()