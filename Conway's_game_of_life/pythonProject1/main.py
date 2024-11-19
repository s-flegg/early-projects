import copy


global cells
cells = [[0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 0],
         [0, 1, 0, 1, 1, 0],
         [0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]
         ]


def print_grid():
    for i, val in enumerate(cells):
        if i % 6 == 0 and i != 0:
            print("\n")
            print(val)
        else:
            print(val)


# Logic
# for cell x, y the surrounding cells are
# x + 1, y
# x - 1, y
# x, y + 1
# x, y - 1


def check_surrounding_alive(x, y):
    """Returns amount alive"""
    alive = 0
    if x != 5:
        if cells[x + 1][y] == 1:
            alive += 1
    if x != 0:
        if cells[x - 1][y] == 1:
            alive += 1
    if y != 5:
        if cells[x][y + 1] == 1:
            alive += 1
    if y != 0:
        if cells[x][y - 1] == 1:
            alive += 1
    return alive


def check_if_keep_living(x, y):
    if check_surrounding_alive(x, y) == 2 or check_surrounding_alive(x, y) == 3:
        return True
    else:
        return False


def check_if_revive(x, y):
    if check_surrounding_alive(x, y) == 3:
        return True
    else:
        return False

def check_any_alive():
    alive = 0
    for x in range(6):
        for y in range(6):
            if cells[x][y] == 1:
                alive += 1
    if alive >= 1:
        return True
    else:
        return False


print_grid()


while check_any_alive():
    new = copy.copy(cells)
    for x in range(6):
        for y in range(6):
            if cells[x][y] == 1:
                if check_if_keep_living(x, y):
                    new[x][y] = 1
                else:
                    new[x][y] = 0
            else:
                if check_if_revive(x, y):
                    new[x][y] = 1
                else:
                    new[x][y] = 0
    cells = new
    print("\n")
    print_grid()