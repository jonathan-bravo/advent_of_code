import numpy as np
from dataclasses import dataclass, field

# these are all the deltas to consider in a 3d grid
# can account for these when checking if the node is a possible move...
# DELTAS = [
#             (1, 0, 0), (-1, 0, 0), # only x
#             (0, 1, 0), (-1, 0, 0), # only y
#             (1, 0, 1), (-1, 0, 1), # x while up z
#             (0, 1, 1), (0, -1, 1), # y while up z
#             (1, 0, -1), (-1, 0, -1), # w while down z
#             (1, 0, -2), (-1, 0, -2),
#             (1, 0, -3), (-1, 0, -3),
#             (1, 0, -4), (-1, 0, -4),
#             (1, 0, -5), (-1, 0, -5),
#             (1, 0, -6), (-1, 0, -6),
#             (1, 0, -7), (-1, 0, -7),
#             (1, 0, -8), (-1, 0, -8),
#             (1, 0, -9), (-1, 0, -9),
#             (1, 0, -10), (-1, 0, -10),
#             (1, 0, -11), (-1, 0, -11),
#             (1, 0, -12), (-1, 0, -12),
#             (1, 0, -13), (-1, 0, -13),
#             (1, 0, -14), (-1, 0, -14),
#             (1, 0, -15), (-1, 0, -15),
#             (1, 0, -16), (-1, 0, -16),
#             (1, 0, -17), (-1, 0, -17),
#             (1, 0, -18), (-1, 0, -18),
#             (1, 0, -19), (-1, 0, -19),
#             (1, 0, -20), (-1, 0, -20),
#             (1, 0, -21), (-1, 0, -21),
#             (1, 0, -22), (-1, 0, -22),
#             (1, 0, -23), (-1, 0, -23),
#             (1, 0, -24), (-1, 0, -24),
#             (1, 0, -25), (-1, 0, -25),
#             (1, 0, -26), (-1, 0, -26),
#             (0, 1, -1), (0, -1, -1), # y while down z
#             (0, 1, -2), (0, -1, -2),
#             (0, 1, -3), (0, -1, -3),
#             (0, 1, -4), (0, -1, -4),
#             (0, 1, -5), (0, -1, -5),
#             (0, 1, -6), (0, -1, -6),
#             (0, 1, -7), (0, -1, -7),
#             (0, 1, -8), (0, -1, -8),
#             (0, 1, -9), (0, -1, -9),
#             (0, 1, -10), (0, -1, -10),
#             (0, 1, -11), (0, -1, -11),
#             (0, 1, -12), (0, -1, -12),
#             (0, 1, -13), (0, -1, -13),
#             (0, 1, -14), (0, -1, -14),
#             (0, 1, -15), (0, -1, -15),
#             (0, 1, -16), (0, -1, -16),
#             (0, 1, -17), (0, -1, -17),
#             (0, 1, -18), (0, -1, -18),
#             (0, 1, -19), (0, -1, -19),
#             (0, 1, -20), (0, -1, -20),
#             (0, 1, -21), (0, -1, -21),
#             (0, 1, -22), (0, -1, -22),
#             (0, 1, -23), (0, -1, -23),
#             (0, 1, -24), (0, -1, -24),
#             (0, 1, -25), (0, -1, -25),
#             (0, 1, -26), (0, -1, -26),
#         ]

# class Node():
#     """A node class for A* Pathfinding"""

#     def __init__(self, parent=None, position=None):
#         self.parent = parent
#         self.position = position

#         self.g = 0
#         self.h = 0
#         self.f = 0

#     def __eq__(self, other):
#         return self.position == other.position

#     def possible_moves(self, map):
#         x, y = self.x, self.y
#         for dx, dy in DELTAS:
#             newx, newy = x + dx, y + dy
#             try:
#                 if maze[newx][newy] <= maze[x][y] + 1:
#                     yield Node(self, (newx, newy))
#             except IndexError:
#                 # not inside the maze anymore, ignore
#                 pass

# def astar(maze, start, end):

#     # Create start and end node
#     start_node = Node(None, start)
#     start_node.g = start_node.h = start_node.f = 0
#     end_node = Node(None, end)
#     end_node.g = end_node.h = end_node.f = 0

#     # Initialize both open and closed list
#     open_list = []
#     closed_list = []

#     # Add the start node
#     open_list.append(start_node)

#     # Loop until you find the end
#     while len(open_list) > 0:
#         # Get the current node
#         current_node = open_list[0]
#         current_index = 0
#         for index, item in enumerate(open_list):
#             if item.f < current_node.f:
#                 current_node = item
#                 current_index = index

#         # Pop current off open list, add to closed list
#         open_list.pop(current_index)
#         closed_list.append(current_node)

#         # Found the goal
#         if current_node == end_node:
#             path = []
#             current = current_node
#             while current is not None:
#                 path.append(current.position)
#                 current = current.parent
#             return path[::-1] # Return reversed path

#         # Generate children
#         children = []

#         for new_position in deltas:

#             # Get node position
#             node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2])

#             # Make sure within range
#             if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0 or node_position[2] > (len(maze) - 1) or node_position[2] < 0 or node_position[2] > (len(maze[len(maze)-1]) -1):
#                 continue

#             # Make sure walkable terrain
#             if maze[node_position[0]][node_position[1]][node_position[2]] != 0:
#                 continue

#             # Create new node
#             new_node = Node(current_node, node_position)

#             # Append
#             children.append(new_node)

#         # Loop through children
#         for child in children:

#             # Child is on the closed list
#             for closed_child in closed_list:
#                 if child == closed_child:
#                     continue

#             # Create the f, g, and h values
#             child.g = current_node.g + 1
#             child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)+((child.position[2] - end_node.position[2]) ** 2)
#             child.f = child.g + child.h

#             # Child is already in the open list
#             for open_node in open_list:
#                 if child == open_node and child.g > open_node.g:
#                     continue

#             # Add the child to the open list
#             open_list.append(child)

DELTAS = [
            (1, 0, 0), (-1, 0, 0), # only x
            (0, 1, 0), (-1, 0, 0) # only y
        ]

@dataclass
class Node():
    position:tuple(int) = field(default_factory=tuple)
    parent:tuple(int) = field(default_factory=tuple)
    g:int = 0
    h:int = 0
    f:int = 0

    def __eq__(self, other):
        return self.position == other.position

    def possible_moves(self, map):
        x, y = self.x, self.y
        for dx, dy in DELTAS:
            newx, newy = x + dx, y + dy
            try:
                if maze[newx][newy] <= maze[x][y] + 1:
                    yield Node(self, (newx, newy))
            except IndexError:
                # not inside the maze anymore, ignore
                pass


def astar(maze, start, end):

    # Create start and end node
    start_node = Node(start)
    end_node = Node(end)

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []

        for new_position in deltas:

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0 or node_position[2] > (len(maze) - 1) or node_position[2] < 0 or node_position[2] > (len(maze[len(maze)-1]) -1):
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]][node_position[2]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)+((child.position[2] - end_node.position[2]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

# to 3d cube
# def parse_matrix(matrix):
#     cube = []
#     for z in range(26):
#         layer = []
#         for i,row in enumerate(matrix):
#             new_row = []
#             for j,val in enumerate(row):
#                 if val == 'S':
#                     if z == 0:
#                         start = (j,i,0)
#                         new_row.append(1)
#                 elif val == 'E':
#                     if z == 0:
#                         end = (j,i,0)
#                         new_row.append(0)
#                 else:
#                     if ord(val) - 96 <= z+1:
#                         new_row.append(1)
#                     else:
#                         new_row.append(0)
#             layer.append(new_row)
#         cube.append(layer)
#     return cube, start, end

def parse_matrix(matrix):
    parsed_matrix = []
    for i,row in enumerate(matrix):
        parsed_row = []
        for j,val in enumerate(row):
            if val == 'S':
                start = (j,i)
                parsed_row.append(1)
            elif val == 'E':
                end = (j,i)
                parsed_row.append(1)
            else:
                parsed_row.append(ord(val) - 96)
        parsed_matrix.append(parsed_row)
    return parsed_matrix, start, end

def main():
    with open('12_input.test.txt') as f:
        matrix = [line.strip() for line in f]
        matrix = [[x for x in string] for string in matrix]
        maze, start, end = parse_matrix(matrix)
        # print(start, end)
        # print(cube[start[0]][start[1]][start[2]])
        # path = astar(cube, start, end)
        # print(path)
        # for layer in cube:
        #     for row in layer:
        #         print(layer)
        #     print()

if __name__ == '__main__':
    main()


