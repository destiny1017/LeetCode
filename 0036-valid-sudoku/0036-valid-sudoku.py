class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i_sets = [set() for _ in range(9)]
        j_sets = [set() for _ in range(9)]
        square_sets = [[set() for _ in range(3)] for _ in range(3)]

        for b in board:
            print(b)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                
                if val in i_sets[i]:
                    return False
                i_sets[i].add(val)
                
                if val in j_sets[j]:
                    return False
                j_sets[j].add(val)

                if val in square_sets[i // 3][j // 3]:
                    return False
                square_sets[i // 3][j // 3].add(val)
    
        return True
                
