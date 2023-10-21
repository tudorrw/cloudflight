def main():
    with open("level1/level1_5.in") as file:
        map_size = int(file.readline())
        matrix = list()
        for _ in range(map_size):
            matrix.append(list(file.readline().strip()))

        nr_coordinates = int(file.readline())

        output = open('level1/level1_5.out', 'w')
        for _ in range(nr_coordinates):
            coordinates = file.readline().strip().split(',')
            print(matrix[int(coordinates[1])][int(coordinates[0])])
            output.write(matrix[int(coordinates[1])][int(coordinates[0])])
            output.write("\n")
        output.close()


if __name__ == '__main__':
    main()