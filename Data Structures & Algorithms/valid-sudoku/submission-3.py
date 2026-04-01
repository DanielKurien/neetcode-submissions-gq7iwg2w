class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            numSet = set()
            for num in row:
                if num != "." and ((int(num) > 9 or int(num) <= 0) or num in numSet):
                    return False
                else:
                    numSet.add(num)
        for j in range(0, len(board)):
            numSet = set()
            for i in range(0, len(board)):
                num = board[i][j]
                if num != "." and ((int(num) > 9 or int(num) <= 0) or num in numSet):
                    return False
                else:
                    numSet.add(num)
        squares = collections.defaultdict(set)
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                index = (i // 3, j // 3)
                if board[i][j] != "." and board[i][j] in squares[index]:
                    return False
                else:
                    squares[index].add(board[i][j])

        return True
