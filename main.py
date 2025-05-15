import sys

BOARD_SIZE = 7
KNIGHT_MOVES = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def print_board(visited, knight_pos):
    for y in range(BOARD_SIZE):
        row = ''
        for x in range(BOARD_SIZE):
            if (x, y) == knight_pos:
                row += ' K '
            elif visited[y][x]:
                row += ' . '
            else:
                row += ' - '
        print(row)
    print()

def is_valid(x, y, visited):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and not visited[y][x]

def get_valid_moves(x, y, visited):
    return [
        (x+dx, y+dy)
        for dx, dy in KNIGHT_MOVES
        if is_valid(x+dx, y+dy, visited)
    ]

def main():
    visited = [[False]*BOARD_SIZE for _ in range(BOARD_SIZE)]
    print('Welcome to the Knight Game (7x7)!')
    try:
        x = int(input('Enter starting X (0-6): '))
        y = int(input('Enter starting Y (0-6): '))
    except ValueError:
        print('Invalid input. Exiting.')
        sys.exit(1)
    if not is_valid(x, y, visited):
        print('Invalid starting position. Exiting.')
        sys.exit(1)
    knight_pos = (x, y)
    visited[y][x] = True
    move_count = 1
    while True:
        print_board(visited, knight_pos)
        moves = get_valid_moves(*knight_pos, visited)
        if not moves:
            print(f'Game over! Total moves: {move_count}')
            break
        print('Valid moves:', moves)
        try:
            nx = int(input('Next X: '))
            ny = int(input('Next Y: '))
        except ValueError:
            print('Invalid input. Exiting.')
            break
        if (nx, ny) not in moves:
            print('Invalid move. Try again.')
            continue
        knight_pos = (nx, ny)
        visited[ny][nx] = True
        move_count += 1

if __name__ == '__main__':
    main()
