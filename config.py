width = 400
height = 400
w = 20
rows = height // w
cols = width // w


def index(i, j):
    if i < 0 or j < 0 or i > cols-1 or j > rows-1:
        return None
    return i + j * cols
