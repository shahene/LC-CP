import collections
class Solution:
    def tictactoe(self, moves: List[List(int)]) -> str:
        turn_a = True
        x_o_map = collections.defaultdict(list)
        # build map
        for move in moves:
            r, c = move
            if turn_a:
                x_o_map['A'].append((r, c))
            else:
                x_o_map['B'].append((r, c))
            turn_a = not turn_a
        '''
        how to check winner

        diagonal
        (0, 0), (1, 1), (2, 2)
        (0, 2), (1, 1), (2, 0)
        
        horizontal
        (0, 0), (0, 1), (0, 2)
        (1, 0), (1, 1), (1, 2)
        (2, 0), (2, 1), (2, 2)

        vertical
        (0, 0), (1, 0), (2, 0)
        (0, 1), (1, 1), (2, 1)
        (0, 2), (1, 2), (2, 2)
        

        basically if any of x or o has all three of these
        wins
        '''
        for n in x_o_map:
            diagonal_1 = {(0, 0), (1, 1), (2, 2)}
            diagonal_2 = {(0, 2), (1, 1), (2, 0)}
            hor_1 = {(0, 0), (0, 1), (0, 2)}
            hor_2 = {(1, 0), (1, 1), (1, 2)}
            hor_3 = {(2, 0), (2, 1), (2, 2)}
            ver_1 = {(0, 0), (1, 0), (2, 0)}
            ver_2 = {(0, 1), (1, 1), (2, 1)}
            ver_3 = {(0, 2), (1, 2), (2, 2)}

            for tup in x_o_map[n]:
                if tup in diagonal_1:
                    diagonal_1.remove((tup))
                    if len(diagonal_1) == 0: return n
                
                if tup in diagonal_2:
                    diagonal_2.remove(tup)
                    if len(diagonal_2) == 0: return n

                if tup in hor_1:
                    hor_1.remove(tup)
                    if len(hor_1) == 0: return n
                if tup in hor_2:
                    hor_2.remove(tup)
                    if len(hor_2) == 0: return n
                if tup in hor_3:
                    hor_3.remove(tup)
                    if len(hor_3) == 0: return n
                if tup in ver_1:
                    ver_1.remove(tup)
                    if len(ver_1) == 0: return n
                if tup in ver_2:
                    ver_2.remove(tup)
                    if len(ver_2) == 0: return n
                if tup in ver_3:
                    ver_3.remove(tup)
                    if len(ver_3) == 0: return n
        return 'Draw' if len(moves) == 9 else 'Pending'
        