import sys
import numpy as np

def read_dict(file_path):
    f = open(file_path, "r")
    dict_text = f.read()
    # print(f.read())
    return dict_text

def get_grid_2d(text, grid_dim=4):
    temp = []
    for i in range(len(grid_text)):
        temp.append(grid_text[i])
    return np.reshape(temp, [-1, grid_dim])


def checkValid(word, dict_text):
    if word in dict_text:
        return True
    else:
        return False

# returns a list of  neighbours
def get_neighbours(row, col, grid):
    M, N = grid.shape
    # for m in range(row, M):
    #     for n in range(col, N):

    return


def perpendicular_str(strH, row, col, grid, words):
    M, _ = grid.shape
    # print('-------------------perpendicular_str--------------------------')
    # print('strH ############### = ', strH)
    per_str = strH
    for m in range(row + 1, M):
        per_str = per_str + grid[m][col]
        if (len(per_str) >= 3) and (per_str in words):
            print('per_str = ', per_str)

    # print(per_str)
    return per_str


if __name__ == "__main__":
    file_path = sys.argv[1]
    grid_text = sys.argv[2]
    grid = get_grid_2d(grid_text)

    words = read_dict(file_path)
    split_words = words.split()
    print('type split_words = ', type(split_words))

    M, N = grid.shape
    # horizontal, vertical
    for row in range(M):
        strH = ''
        strV = ''
        for col in range(N):
            strH = strH + grid[row][col]
            perpendicular_str(strH, row, col, grid, words)
            strV = strV + grid[col][row]
            if (len(strH) >= 3) and (strH in split_words):
                print("str = ", strH)
            if (len(strV) >= 3) and (strV in split_words):
                print('strV = ', strV)
