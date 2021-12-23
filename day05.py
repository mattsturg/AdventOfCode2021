from typing import List


class Line:
    min = 0
    max = 0
    other_pos = 0
    x_axis = False
    straight = True
    left_x = 0
    left_y = 0
    range = 0
    positive_slope = False

    def __init__(self, line_str: str):
        coordinates = line_str.split(' -> ')
        coordinates_halves = coordinates[0].split(',')
        coordinates_halves.append(coordinates[1].split(',')[0])
        coordinates_halves.append(coordinates[1].split(',')[1])
        if int(coordinates_halves[0]) == int(coordinates_halves[2]):
            self.other_pos = int(coordinates_halves[0])
            if int(coordinates_halves[1]) < int(coordinates_halves[3]):
                self.min = int(coordinates_halves[1])
                self.max = int(coordinates_halves[3])
            else:
                self.min = int(coordinates_halves[3])
                self.max = int(coordinates_halves[1])
        elif int(coordinates_halves[1]) == int(coordinates_halves[3]):
            self.other_pos = int(coordinates_halves[1])
            self.x_axis = True
            if int(coordinates_halves[0]) < int(coordinates_halves[2]):
                self.min = int(coordinates_halves[0])
                self.max = int(coordinates_halves[2])
            else:
                self.min = int(coordinates_halves[2])
                self.max = int(coordinates_halves[0])
        else:
            self.straight = False
            if int(coordinates_halves[0]) < int(coordinates_halves[2]):
                self.left_x = int(coordinates_halves[0])
                self.left_y = int(coordinates_halves[1])
                self.range = int(coordinates_halves[2]) - int(coordinates_halves[0])
                if int(coordinates_halves[1]) > int(coordinates_halves[3]):
                    self.positive_slope = True
            else:
                self.left_x = int(coordinates_halves[2])
                self.left_y = int(coordinates_halves[3])
                self.range = int(coordinates_halves[0]) - int(coordinates_halves[2])
                if int(coordinates_halves[3]) > int(coordinates_halves[1]):
                    self.positive_slope = True


def find_graph_dimensions(lines: List):
    x_max = 0
    y_max = 0
    for line in lines:
        if line.straight:
            if line.x_axis:
                if line.max > x_max:
                    x_max = line.max
                if line.other_pos > y_max:
                    y_max = line.other_pos
            else:
                if line.max > y_max:
                    y_max = line.max
                if line.other_pos > x_max:
                    x_max = line.other_pos
        else:
            if line.positive_slope:
                if line.left_x + line.range > x_max:
                    x_max = line.left_x + line.range
                if line.left_y > y_max:
                    y_max = line.left_y
            else:
                if line.left_x + line.range > x_max:
                    x_max = line.left_x + line.range
                if line.left_y + line.range > y_max:
                    y_max = line.left_y + line.range
    return x_max, y_max


def graph_lines(graph: List, lines: List):
    for line in lines:
        if line.straight:
            if line.x_axis:
                for index in range(line.min, line.max+1):
                    if graph[line.other_pos][index] == '.':
                        graph[line.other_pos][index] = 1
                    else:

                        graph[line.other_pos][index] += 1
            else:
                for index in range(line.min, line.max+1):
                    if graph[index][line.other_pos] == '.':
                        graph[index][line.other_pos] = 1
                    else:

                        graph[index][line.other_pos] += 1
    return graph


def graph_lines_with_diagonals(graph: List, lines: List):
    for line in lines:
        if line.straight:
            if line.x_axis:
                for index in range(line.min, line.max+1):
                    if graph[line.other_pos][index] == '.':
                        graph[line.other_pos][index] = 1
                    else:
                        graph[line.other_pos][index] += 1
            else:
                for index in range(line.min, line.max+1):
                    if graph[index][line.other_pos] == '.':
                        graph[index][line.other_pos] = 1
                    else:
                        graph[index][line.other_pos] += 1
        else:
            if line.positive_slope:
                for index in range(0, line.range+1):
                    if graph[line.left_y-index][line.left_x+index] == '.':
                        graph[line.left_y-index][line.left_x+index] = 1
                    else:
                        graph[line.left_y-index][line.left_x+index] += 1
            else:
                for index in range(0, line.range+1):
                    if graph[line.left_y+index][line.left_x+index] == '.':
                        graph[line.left_y+index][line.left_x+index] = 1
                    else:
                        graph[line.left_y+index][line.left_x+index] += 1
    return graph


def count_overlaps(graph: List):
    count = 0
    for row in graph:
        for item in row:
            if item == '.':
                count = count
            elif item > 1:
                count += 1
    return count


def grid_building(lines: List) -> int:
    new_lines = []
    for item in lines:
        new_lines.append(Line(item))
    dimensions = find_graph_dimensions(new_lines)
    graph = []
    for index in range(0, dimensions[1]+1):
        my_list = []
        for index_two in range(dimensions[0]+1):
            my_list.append('.')
        graph.append(my_list)

    graph = graph_lines(graph, new_lines)
    return count_overlaps(graph)


def grid_building_with_diagonals(lines: List) -> int:
    new_lines = []
    for item in lines:
        new_lines.append(Line(item))
    dimensions = find_graph_dimensions(new_lines)
    graph = []
    for index in range(0, dimensions[1]+1):
        my_list = []
        for index_two in range(dimensions[0]+1):
            my_list.append('.')
        graph.append(my_list)

    graph = graph_lines_with_diagonals(graph, new_lines)

    # for rows in graph:
    #     print()
    #     for item in rows:
    #         print(item, end='')

    return count_overlaps(graph)
