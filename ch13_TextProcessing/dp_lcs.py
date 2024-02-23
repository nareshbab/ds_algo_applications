import sys

## ------------------dynamic programming recursive----------------##

def lcs(X, Y, m, n):

    if m==0 or n==0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1+ lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m-1, n), lcs(X, Y, m, n-1))
    
X = "AGGTAB"
Y = "GXTXAYB"
# print ("Length of LCS is ", lcs(X, Y, len(X), len(Y)))

##-----------------dynamic programming recursive with memoization -------------#
n = len(Y)
m = len(X)
dp = [[-1 for a in range(n+1)] for b in range(m+1)]

def lcs_memo(X: str, Y: str, m: int, n: int, dp: list) -> int:

    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        dp[m][n] = 1 + lcs_memo(X, Y, m-1, n-1, dp)
        return dp[m][n]
    else:
        dp[m][n] = max(lcs_memo(X, Y, m-1, n, dp), lcs_memo(X, Y, m, n-1, dp))
    return dp[m][n]

# print ("Length of LCS is ", lcs_memo(X, Y, len(X), len(Y), dp))


##-----------------dynamic programming using bottom up (tabulation) ---------------------------#




def lcs_tabulation(X: str, Y: str, m: int, n: int):

    dp = [[-1 for a in range(n+1)] for b in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n] 

print ("Length of LCS is ", lcs_tabulation(X, Y, len(X), len(Y)))