def cross(coordinates):
    # print(coordinates)
    if (coordinates[0][0], coordinates[0][1]) in coordinates[1:]:
        # print(coordinates[0])
        # print(coordinates[0 + 1:])
        return False

    for i in range(1,len(coordinates)):
        # print(coordinates[i])
        if (coordinates[i][0],coordinates[i][1]) in coordinates[i+1:]:
            # print(coordinates[i])
            # print(coordinates[i+1:])
            return False
        if abs(coordinates[i - 1][0] - coordinates[i][0]) == 1 and abs(coordinates[i - 1][1] - coordinates[i][1]) == 1:
            # print(coordinates[i-1],coordinates[i])
            if(coordinates[i-1][0]-coordinates[i][0] == -1) and (coordinates[i-1][1]-coordinates[i][1] == -1):
                # print(coordinates[i])
                if(coordinates[i][0],coordinates[i][1]-1) in coordinates and (coordinates[i][0]-1,coordinates[i][1]) in coordinates:
                    # print(coordinates.index((coordinates[i][0],coordinates[i][1]-1)))
                    if abs(coordinates.index((coordinates[i][0], coordinates[i][1] - 1)) - coordinates.index((coordinates[i][0] - 1, coordinates[i][1])))==1:
                        return False
            if(coordinates[i-1][0]-coordinates[i][0] == 1) and (coordinates[i-1][1]-coordinates[i][1] == 1):
                if(coordinates[i][0],coordinates[i][1]+1) in coordinates and (coordinates[i][0]+1,coordinates[i][1]) in coordinates and abs(coordinates.index((coordinates[i][0],coordinates[i][1]+1))-coordinates.index((coordinates[i][0]+1,coordinates[i][1])))==1:
                    return False

            if (coordinates[i - 1][0] - coordinates[i][0] == -1) and (coordinates[i - 1][1] - coordinates[i][1] == 1):
                if (coordinates[i][0]-1, coordinates[i][1]) in coordinates and (
                coordinates[i][0], coordinates[i][1]+1) in coordinates:
                    if abs(
                        coordinates.index((coordinates[i][0]-1, coordinates[i][1])) - coordinates.index((
                                coordinates[i][0], coordinates[i][1]+1))) == 1:
                        return False

            if (coordinates[i - 1][0] - coordinates[i][0] == 1) and (coordinates[i - 1][1] - coordinates[i][1] == -1):
                if (coordinates[i][0], coordinates[i][1]-1) in coordinates and (
                        coordinates[i][0]+1, coordinates[i][1]) in coordinates:
                    if abs(
                    coordinates.index((coordinates[i][0], coordinates[i][1]-1)) - coordinates.index(
                        (coordinates[i][0]+1, coordinates[i][1]))) == 1:
                        return False
    return True

def main():
    with open("level3/level3_5.in") as file:
        map_size = int(file.readline())
        matrix = list()
        for _ in range(map_size):
            matrix.append(list(file.readline().strip()))
        nr_coordinates = int(file.readline())
        output = open('level3/level3_5.out', 'w')
        for _ in range(nr_coordinates):
            coordinates = file.readline().split()
            coordinates = list(map(lambda x: (int(x[0]), int(x[1])), list(map(lambda x: x.split(','), coordinates))))
            if(cross(coordinates)):
                # print("VALID")
                output.write("VALID\n")
            else:
                # print("INVALID")
                output.write("INVALID\n")
        output.close()
if __name__ == '__main__':
    main()