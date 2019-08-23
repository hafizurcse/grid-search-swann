import sys
import numpy as np 

def read_dict(file_path):
    f = open(file_path, "r")
    dict_text = f.read()
    print(f.read())
    return dict_text

def get_grid_2d(text):
    temp = []
    for i in range(len(grid_text)):
        temp.append(grid_text[i])
    return np.reshape(temp, [-1, 4])


def checkValid(word, dict_text):
    if word in dict_text:
        return True
    else:
        return False

# returns a list of  neighbours
def get_neighbours(char, grid):
    return


if __name__ == "__main__":
    file_path = sys.argv[1]
    grid_text = sys.argv[2]
    grid = get_grid_2d(grid_text)
    print("grid = ", grid)

    words = read_dict(file_path)
    print("words = ", words)


    for row in range(4):
        for col in range(4): 
            neighbours = get_neighbours(row, col)
    