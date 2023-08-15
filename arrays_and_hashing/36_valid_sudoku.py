from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row cannot have 1-9 repeated
        # column cannot have 1-9 repeated
        # 3x3s cannot have 1-9 repeated

        # Solution 1:

        # Time Complexity:
        # Space Complexity:

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
                # in that row. If not, append it to that row since we've seen it now.
                if i in rows:
                    if board[i][j] in rows[i]:
                        return False
                    rows[i].append(board[i][j])

                # if the row was not added yet, we add the current value to the array (setup)
                else:
                    rows[i] = [board[i][j]]

                # same explanation as above
                if j in columns:
                    if board[i][j] in columns[j]:
                        return False
                    columns[j].append(board[i][j])
                else:
                    columns[j] = [board[i][j]]

                # same explanation as above
                # every number in a 3x3 box falls into floor division of (i // 3, j // 3)
                if (i // 3, j // 3) in boxes:

                    if board[i][j] in boxes[(i // 3, j // 3)]:
                        return False
                    boxes[(i // 3, j // 3)].append(board[i][j])
                else:
                    boxes[(i // 3, j // 3)] = [board[i][j]]

        return True

