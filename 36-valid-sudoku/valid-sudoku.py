class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check, col check, sub-box check
        valid_check_rows = collections.defaultdict(set)
        valid_check_cols = collections.defaultdict(set)
        valid_check_subbox = collections.defaultdict(set)
        
        dim = len(board)
        for r in range(len(board)):
            for c in range(len(board)):        
                val = board[r][c]
                if val == '.': continue
                if val in valid_check_rows[r] or val in valid_check_cols[c] or val in valid_check_subbox[(r // 3, c // 3)]:
                    return False
                valid_check_rows[r].add(board[r][c])
                valid_check_cols[c].add(board[r][c])
                valid_check_subbox[(r // 3, c // 3)].add(board[r][c])
        return True