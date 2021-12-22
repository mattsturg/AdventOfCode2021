from typing import List


def search_columns(current_board: List, list_of_marks: List):
    small_mark_list = []
    count = 1
    for mark in list_of_marks:
        small_mark_list.append(mark)
        found = column_check(current_board, small_mark_list)
        if found:
            return count
        count += 1
    return count


def column_check(current_board: List, small_mark_list: List):
    for index_column in range(5):
        whole_row_marked = True
        for index_row in range(5):
            found = False
            for mark in small_mark_list:
                if mark == current_board[index_row][index_column]:
                    found = True
            if not found:
                whole_row_marked = False
        if whole_row_marked:
            return True
    return False


def row_check(current_board: List, small_mark_list: List):
    for row in current_board:
        whole_row_marked = True
        for number in row:
            found = False
            for mark in small_mark_list:
                if mark == number:
                    found = True
            if not found:
                whole_row_marked = False
        if whole_row_marked:
            return True
    return False


def search_rows(current_board: List, list_of_marks: List):
    small_mark_list = []
    count = 1
    for mark in list_of_marks:
        small_mark_list.append(mark)
        found = row_check(current_board, small_mark_list)
        if found:
            return count
        count += 1
    return count


def full_board_test(current_board: List, list_of_marks: List):
    count_one = search_columns(current_board, list_of_marks)
    count_two = search_rows(current_board, list_of_marks)
    if count_one < count_two:
        return count_one
    else:
        return count_two


def count_unmarked(current_board: List, list_of_marks: List, max_mark: int):
    total = 0
    for row in current_board:
        for number in row:
            found = False
            for index in range(0, max_mark):
                # print(number + "=" + list_of_marks[index])
                if number == list_of_marks[index]:
                    found = True
            if not found:
                total += int(number)
    # print(total)
    return total


def bingo(boards: List) -> int:
    first = True
    list_of_marks = []
    current_board = [[]] * 5
    count = 5
    best = [100, 0]
    for line in boards:
        if first:
            first = False
            list_of_marks = line.split(",")
        else:
            if count == 5:
                count = 0
            else:
                current_board[count] = line.split()
                if count == 4:
                    last_board = full_board_test(current_board, list_of_marks)
                    if last_board < best[0]:
                        best[0] = last_board
                        best[1] = count_unmarked(current_board, list_of_marks, best[0])
                count += 1
    return int(list_of_marks[best[0]-1])*best[1]


def bingo_loose(boards: List) -> int:
    first = True
    list_of_marks = []
    current_board = [[]] * 5
    count = 5
    best = [0, 0]
    for line in boards:
        if first:
            first = False
            list_of_marks = line.split(",")
        else:
            if count == 5:
                count = 0
            else:
                current_board[count] = line.split()
                if count == 4:
                    last_board = full_board_test(current_board, list_of_marks)
                    if last_board > best[0]:
                        best[0] = last_board
                        best[1] = count_unmarked(current_board, list_of_marks, best[0])
                count += 1
    return int(list_of_marks[best[0]-1])*best[1]
