class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        use set for columns, set for rows, and set for 3*3 boxes
        3*3 boxes -> key for set will be (r // 3, c // 3) as tuple 
        O(81) -> O(81) time O(9) space -> O(1) time and O(1) space
        '''
        row_set, col_set, box_set = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in box_set[(r // 3, c // 3)]:
                    return False
                if board[r][c] != '.':
                    row_set[r].add(board[r][c])
                    col_set[c].add(board[r][c])
                    box_set[(r // 3, c // 3)].add(board[r][c])
        return True

