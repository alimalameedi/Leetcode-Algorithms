from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row cannot have 1-9 repeated
        # column cannot have 1-9 repeated
        # 3x3s cannot have 1-9 repeated

        # Solution 1:

        # Time Complexity: O(1) since we are only ever going to have a 9x9 board.
        # Space Complexity: O(1) since we only ever have 81 iterations/values max to be stored or looked at.
        # If we were having 'n' input or board sizes, this would turn to O(N) for both operations.

        rows = {}
        columns = {}
        boxes = {}

        # loop through the board
        for i in range(9):  # rows
            for j in range(9):  # columns

                # if the spot is unoccupied, we don't consider it
                if board[i][j] == ".":
                    continue

                # if the row has been registered in our map, check if the value on the board has already been used
                # in that row. If not, add to that row since we've seen it now.
                if i in rows:
                    if board[i][j] in rows[i]:
                        return False
                    rows[i][board[i][j]] = 1

                # if the row was not added yet, we add the current value to the array (setup)
                else:
                    rows[i] = {board[i][j]: 1}

                # same explanation as above
                if j in columns:
                    if board[i][j] in columns[j]:
                        return False
                    columns[j][board[i][j]] = 1
                else:
                    columns[j] = {board[i][j]: 1}

                # same explanation as above
                # every number in a 3x3 box falls into floor division of (i // 3, j // 3)
                if (i // 3, j // 3) in boxes:

                    if board[i][j] in boxes[(i // 3, j // 3)]:
                        return False
                    boxes[(i // 3, j // 3)][board[i][j]] = 1
                else:
                    boxes[(i // 3, j // 3)] = {board[i][j]: 1}

        return True
