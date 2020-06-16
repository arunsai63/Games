def valid(board):
    for row, col in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]: # blocks
        numbers = [board[row+i][col+j] for i in range(3) for j in range(3) if board[row+i][col+j]]
        if len(set(numbers)) != len(numbers):
            return False
            
    for row in board: # rows
        numbers = [num for num in row if num]
        if len(set(numbers)) != len(numbers):
            return False

    for col in range(9): # cols
        numbers = [board[num][col] for num in range(9) if board[num][col]]
        if len(set(numbers)) != len(numbers):
            return False

    return True

def solve(board): # back-tracking algorithm
    for row in range(9):
        for col in range(9):
            if not board[row][col]:
                for num in range(1,10):
                    board[row][col] = num
                    if valid(board) and solve(board):
                        return True
                board[row][col] = 0            
                return False
    return True