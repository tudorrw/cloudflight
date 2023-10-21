from collections import deque
def lee_algorithm(matrix, start, end):
    if(start == end):
        return True
    queue = deque()
    visited = set()
    distance = {start: 0}
    prev = {}

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()

        # Explore the neighboring nodes
        for neighbor in get_neighbors(matrix, node):
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                prev[neighbor] = node
                queue.append(neighbor)

            if neighbor == end:
                return get_shortest_path(prev, start, end)

    return None

def get_neighbors(matrix, node):
    neighbors = []
    row, col = node

    # Check the top neighbor

    if row > 0 and matrix[row - 1][col] == 'W':
        neighbors.append((row - 1, col))

    # Check the bottom neighbor
    if row < len(matrix) - 1 and matrix[row + 1][col] == 'W':
        neighbors.append((row + 1, col))

    # Check the left neighbor
    if col > 0 and matrix[row][col - 1] != 'W':
        neighbors.append((row, col - 1))

    # Check the right neighbor
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 'W':
        neighbors.append((row, col + 1))

    if row > 0 and col>0 and matrix[row - 1][col - 1] == 'W':
        neighbors.append((row - 1, col - 1))

    if row < len(matrix[0])-1 and col < len(matrix[0])-1 and matrix[row + 1][col + 1] == 'W':
        neighbors.append((row + 1, col + 1))

    if row > 0 and col < len(matrix[0])-1 and matrix[row - 1][col + 1] == 'W':
        neighbors.append((row - 1, col + 1))

    if row < len(matrix[0])-1 and col > 0 and matrix[row + 1][col - 1] == 'W':
        neighbors.append((row + 1, col - 1))

    return neighbors

def get_shortest_path(prev, start, end):
    path = []
    node = end

    while node != start:
        path.append(node)
        node = prev[node]

    path.append(start)
    path.reverse()
    return path

# Testing the implementation


def main():
    with open("level4/level4_5.in") as file:
        map_size = int(file.readline())
        matrix = list()
        for _ in range(map_size):
            matrix.append(list(file.readline().strip()))
        nr_coordinates = int(file.readline())
        output = open('level4/level4_5.out', 'w')
        for _ in range(nr_coordinates):
            coordinates = file.readline().split()
            coordinates[0] = coordinates[0].split(',')
            coordinates[1] = coordinates[1].split(',')
            # print((int(coordinates[0][1]), int(coordinates[0][0])), (int(coordinates[1][1]), int(coordinates[1][0])))
            path = lee_algorithm(matrix, (int(coordinates[0][1]), int(coordinates[0][0])), (int(coordinates[1][1]), int(coordinates[1][0])))
            # print(' '.join([str(t) for t in path]))
            if path != None and len(path) !=map_size*2:
                # output.write(path)
                for tuple in path:
                    # print(str(tuple[1])+","+str(tuple[0]))
                    output.write(str(tuple[1])+","+str(tuple[0])+" ")

            output.write("\n")
        output.close()

if __name__ == '__main__':
    main()