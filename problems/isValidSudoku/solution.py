from typing import List

class IsValidSudoku:
    def solve(self, board: List[List[str]]) -> bool:
        rowSet = set()
        colSet = set()
        boxSet = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue

                boxNo = (i // 3) * 3 + ((j // 3) + 1)

                if (i, board[i][j]) in rowSet or (j, board[i][j]) in colSet or (boxNo, board[i][j]) in boxSet:
                    return False

                rowSet.add((i, board[i][j]))
                colSet.add((j, board[i][j]))
                boxSet.add((boxNo, board[i][j]))

        return True
