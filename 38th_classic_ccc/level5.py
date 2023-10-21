from collections import deque
def lee_algorithm(matrix, start):
    water_total = []
    queue = deque()
    visited = set()
    distance = {start: 0}
    prev = {}

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()

        # Explore the neighboring nodes
        neighbors,waters=get_neighbors(matrix,node)
        print(waters)
        for water in waters:
            if water not in water_total:
                water_total.append(water)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                prev[neighbor] = node
                queue.append(neighbor)
    return water_total


def pathing(borders):
    visited = []
    path = []
    print(borders)
    current = borders[0]
    while(len(visited) != len(borders)):
        for water in borders:
            # print(len(visited))
            # print(len(borders))
            if borders.index(water) not in visited:
                if abs(current[0] -water[0]) == 1 or abs(current[1] - water[1]) == 1:
                    visited.append(borders.index(water))
                    path.append(water)
                    current = water
    return path


def get_neighbors(matrix, node):
    neighbors = []
    borders = []
    row, col = node

    # Check the top neighbor
    if row > 0:
        if matrix[row - 1][col] != 'W':
            neighbors.append((row - 1, col))
        elif (row - 1, col) in borders:
            borders.append((row - 1, col))

    # Check the bottom neighbor
    if row < len(matrix) - 1:
        if matrix[row + 1][col] != 'W':
            neighbors.append((row + 1, col))
        if (row + 1, col) not in borders:
            borders.append((row + 1, col))

    # Check the left neighbor
    if col > 0:
        if matrix[row][col - 1] != 'W':
            neighbors.append((row, col-1))
        if (row, col-1) not in borders:
            borders.append((row, col-1))

    # Check the right neighbor
    if col < len(matrix[0]) - 1:
        if matrix[row][col + 1] != 'W':
            neighbors.append((row, col + 1))
        elif (row, col + 1) not in borders:
            borders.append((row, col + 1))

    return neighbors, borders

def get_shortest_path(prev, start, end):
    path = []
    node = end

    while node != start:
        path.append(node)
        node = prev[node]

    path.append(start)
    path.reverse()
    if path is None:
        return False
    else:
        return True

# Testing the implementation


def main():
    with open("level5/level5_example.in") as file:
        map_size = int(file.readline())
        matrix = list()
        for _ in range(map_size):
            matrix.append(list(file.readline().strip()))
        nr_coordinates = int(file.readline())
        output = open('level2/level5_ex.out', 'w')
        for _ in range(nr_coordinates):
            coordinates = file.readline().split(',')
            borders = lee_algorithm(matrix, (int(coordinates[0]), int(coordinates[1])))
            path = pathing(borders)

            print(path)
        output.close()
if __name__ == '__main__':
    main()