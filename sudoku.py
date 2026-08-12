import random
import copy

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
            
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

def fill_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def generate_puzzle(difficulty_holes=30):
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    
    solution = copy.deepcopy(board)
    puzzle = copy.deepcopy(board)
    
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    
    for i, j in cells[:difficulty_holes]:
        puzzle[i][j] = 0
        
    return puzzle, solution