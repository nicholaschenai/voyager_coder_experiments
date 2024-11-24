

def find_perfect_squares(n):
    squares = []
    i = 1
    while True:
        square = (i * i)
        if (square < n):
            squares.append(square)
        else:
            break
        i += 1
    return squares
