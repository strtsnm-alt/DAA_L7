def isSafe(n, j, q):
    global N
    count=0
    if (n==0 and j==0):
        return True
    for i in range(N):
        if q[i][j]==1:
            count+=1
    for i in range(N):
        if q[n][i]==1:
            count+=1
    j1=i
    n1=n
    while (n1>=0 and j1>=0):
        if q[n1][j1]==1:
            count+=1
        n1-=1
        j1-=1
    j1=i
    n1=n
    while (n1<N and j1<N):
        if q[n1][j1]==1:
            count+=1
        n1+=1
        j1+=1
    j1=i
    n1=n
    while (n1<N and j1>=0):
        if q[n1][j1]==1:
            count+=1
        n1+=1
        j1-=1
    j1=i
    n1=n
    while (n1>=0 and j1<N):
        if q[n1][j1]==1:
            count+=1
        n1-=1
        j1+=1

    if count>6:
        return False
    else:
        return True
N = 4
q = [[0 for _ in range(N)] for _ in range(N)]
def queens(n, q):
    global N
    if n>=N:
        return
    for j in range(N):
        q[n][j] = 1
        if isSafe(n, j, q):
            queens(n+1, q)
        if j==3:
            if n==3:
                print("True")
                print(q)
                exit()
            print("False")
            q[n][j] = 0
            return
        q[n][j] = 0

queens(0, q)
