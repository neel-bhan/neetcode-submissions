class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colums = defaultdict(set)
        rows = defaultdict(set)
        box = defaultdict(set)
        br = 0
        bc = 0

        for r in range(9):
            if r % 3 == 0:
                br +=1
            for c in range(9):
                if c % 3 == 0:
                    bc += 1

                ele = board[r][c]
                if ele == '.':
                    continue
                if ele in rows[r] or ele in colums[c] or ele in box[(br * 3) + bc]:
                    return False
                rows[r].add(ele)
                colums[c].add(ele)
                box[(br * 3) + bc].add(ele)
            bc = 0
        return True