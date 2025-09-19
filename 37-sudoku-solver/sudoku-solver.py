class Solution:
    def solveSudoku(self, board):
        # Track used numbers in rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets and collect empty positions
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empties.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def backtrack(idx=0):
            if idx == len(empties):
                return True  # solved

            r, c = empties[idx]
            b = (r // 3) * 3 + c // 3  # box index

            for ch in "123456789":
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                    # Place number
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[b].add(ch)

                    if backtrack(idx + 1):
                        return True

                    # Undo choice
                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[b].remove(ch)

            return False

        backtrack()
