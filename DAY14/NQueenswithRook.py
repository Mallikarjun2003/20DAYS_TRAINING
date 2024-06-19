def solveNQueens( queens,n: int,rr,rc):
    
    board = [["."]*(n) for _ in range(n)]
    rows , cols , pdiag ,ndiag =set(),set(),set(),set()
    solutions = False
    rookr ,rookc = rr,rc

    def bt(i,queens):
        nonlocal solutions
        if not queens:
            solutions = True
            return
        if i == n:
            return
        for j in range(n):
            if solutions:return True
            if i in rows or j in cols or i+j in pdiag or i-j in ndiag or i==rookr or j == rookc :continue
            board[i][j] = "Q"
            rows.add(i)
            cols.add(j)
            pdiag.add(i+j)
            ndiag.add(i-j)
            bt(i+1,queens-1)
            board[i][j] = "."
            rows.remove(i)
            cols.remove(j)
            pdiag.remove(i+j)
            ndiag.remove(i-j)
        bt(i+1,queens)
            
    bt(0,queens)
    # print(len(solutions))
    return solutions

n = int(input("Enter n Value"))
rookr = int(input("Enter rook row :"))
rookc = int(input("Enter rook col"))
max_queens = 0
for i in range(1,n+1):
    if solveNQueens(i,n,rookr,rookc):
        max_queens = i
print(max_queens)

