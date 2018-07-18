from random import randrange
class Board:
    def __init__(self, N):
        self.N = N
        self.grid = [['H' for _ in range(N)] for _ in range(N)]

        self.bombs = set()
        difficulty = 0.1
        num_of_bombs = int(N * N * difficulty)
        for i in range(num_of_bombs+1):
            self.bombs.add((randrange(N), randrange(N)))
        self.to_reveal = N * N - len(self.bombs)


    def put(self, pos):
        i, j = pos

        if 0 <= i < self.N and 0 <= j < self.N and self.grid[i][j] == 'H':
            # when the cell has a bomb
            if (i, j) in self.bombs:
                self.grid[i][j] = '*'
                return -1
            else: # when the cell does NOT have a bomb
                vectors = [(1, 1), (1, 0), (1, -1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
                queue = [(i, j)]
                visited = set()
                while queue:
                    _i, _j = queue.pop(0)
                    self.to_reveal -= 1
                    visited.add((_i, _j))

                    bombn = sum([(_i + v[0], _j + v[1]) in self.bombs for v in vectors if 0 <= _i + v[0] < self.N and  0 <= _j + v[1] < self.N ])
                    if bombn == 0:
                        self.grid[_i][_j] = '.'
                        for v in vectors:
                            if 0 <= _i + v[0] < self.N and 0 <= _j + v[1] < self.N and (_i + v[0], _j + v[1]) not in visited:
                                queue.append((_i + v[0], _j + v[1]))
                    else:
                        self.grid[_i][_j] = str(bombn)
                return 1
        else: # invalid input are given, 1) out of boundary, 2)the cell is already revealed.
            return 0

    def print_grid(self):
        print('\n'.join(([','.join(row) for row in self.grid])))

class Game:
    def __init__(self):
        self.board = None

    def play(self):
        size = input("Enter size N for grid N*N: ")
        self.board = Board(int(size))

        # just for debugging purpose, should be removed in production
        print(self.board.bombs)

        while self.board.to_reveal > 0:
            row = input("Enter a row: ")
            col = input("Enter a column: ")
            result = self.board.put((row, col))
            print(self.board.print_grid())
            if result == -1:
                print("You lost!")
                return
            elif result == 0:
                print("Invalid input")

        print("You won!")
        print(self.board.print_grid())
        return

g = Game()
g.play()






