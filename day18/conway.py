import sys


def count_neighbords(board, x, y):
    neighbords = (
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
    )

    count = 0

    for n_x, n_y in neighbords:
        if n_x < 0 or n_y < 0:
            continue
        if n_y >= len(board) or n_x >= len(board[0]):
            continue
        count += board[n_y][n_x]

    return count


def get_next_cell_state(board, x, y):
    neighbords = count_neighbords(board, x, y)
    
    if not board[y][x]:
        return 1 if neighbords == 3 else 0
    else:
        return 1 if neighbords == 2 or neighbords == 3 else 0


def game_of_life(board, iterations=1):
    for iteration in xrange(iterations):
        board = [[get_next_cell_state(board, x, y) for x in xrange(len(board[y]))] for y in xrange(len(board))]
    return board


if __name__ == '__main__':
    board = []
    for line in open(sys.argv[1], 'r'):
        board.append([1 if char == '#' else 0 for char in line.strip()])


    final_board = game_of_life(board, iterations=int(sys.argv[2]))
    print(sum([sum(row) for row in final_board]))

