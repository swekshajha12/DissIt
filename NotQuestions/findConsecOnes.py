def find_consecutive_ones_positions(lst):
    consecutive_ones = []
    start = None

    for i, val in enumerate(lst):
        print(i)
        if val == 1:
            if start is None:
                start = i
        else:
            if start is not None:
                consecutive_ones.append([start, i - 1])
                start = None

    if start is not None:
        consecutive_ones.append([start, len(lst) - 1])

    return consecutive_ones


input_list = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
result = find_consecutive_ones_positions(input_list)
print(result)