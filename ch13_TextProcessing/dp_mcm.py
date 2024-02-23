import sys

### ------ Matrix Chain Multiplication ---------###


# Matrix A[i] has dimension p[i-1] x p[i]
# for i in 1...n
def matrix_chain_order(p, i, j):

    if i==j:
        return 0
    
    _min = sys.maxsize

    """
        Place parenthesis at different places
        between first and last matrix
        recursively calculate the cost of multiplications
        for each parenthesis placement
        and return the minimum count
    """

    for k in range(i, j):
        cost = (matrix_chain_order(p, i, k)
        + matrix_chain_order(p, k+1, j)
        + p[i-1]*p[k]*p[j])

        if cost < _min:
            _min = cost

    return _min


# arr = [1,2,3,4,3]
# n=len(arr)

# print("Minimum order of multiplication is ", matrix_chain_order(arr, 1, n-1))


##-------Dynamic Programming Solution using iterative matrix approach--------#

# Matrix A[i] has dimension p[i-1]xp[i] for i=1....n
def matrix_chain_order_dp(p, n):

    m = [[0]*n for x in range(n)]

    """
    m[i,j] = Minimum number of scaler multiplications needed
    to compute the matrix A[i]A[i+1]....A[j] = A[i....j]
    where dimension of A[i] is p[i-1]xp[i]
    """

    # cost of multiplying one matrix is always 0

    for i in range(n):
        m[i][i] = 0

    for b in range (1, n):
        for i in range(n-b):
            j = i+b
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]

                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n-1]


# arr = [1,2,3,4,3]
# n = len(arr)

# print("Minimum number of multiplications is", matrix_chain_order_dp(arr, n))


##-------Dynamic Programming Solution using recursive memoization approach--------#

dp = [[-1 for x in range(100)] for y in range(100)]

def matrix_chain_order_dp_memo(arr, i, j):

    if i==j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    dp[i][j] = sys.maxsize

    for k in range(i, j):
        dp[i][j] = min(dp[i][j], matrix_chain_order_dp_memo(arr, i, k) + matrix_chain_order_dp_memo(arr, k+1, j) + arr[i-1]*arr[k]*arr[j])

    return dp[i][j]


arr = [1,2,3,4,3]
n = len(arr)

print("Minimum number of multiplications is", matrix_chain_order_dp_memo(arr, 1, n-1))
