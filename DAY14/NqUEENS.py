def solveNQueens( n: int):

    board = [["."]*(n-1) for _ in range(n-1)]
    rows , cols , pdiag ,ndiag =set(),set(),set(),set()
    solutions = []
    
    def bt(i):
        nonlocal solutions
        if i == n-1:
            temp=[]
            for row in board:
                temp.append("".join(row))
            if temp not in solutions:    
                solutions.append(temp[:])
            return
        for j in range(n-1):
            if i in rows or j in cols or (i+j) in pdiag or i-j in ndiag :continue
            board[i][j] = "Q"
            rows.add(i)
            cols.add(j)
            pdiag.add(i+j)
            ndiag.add(i-j)
            bt(i+1)
            board[i][j] = "."
            rows.remove(i)
            cols.remove(j)
            pdiag.remove(i+j)
            ndiag.remove(i-j)
    bt(0)
    print(len(solutions))
    return solutions

n = int(input())

solveNQueens(n)