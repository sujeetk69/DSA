"""
On an M x N grid a traveller can either move down or right.
The traveller starts at the top-left corner and wants to reach bottom-right corner.
Write a function which can return number of unique paths a traveller can take.

Constraints:
    1. M > 0
    2. N > 0
"""
from typing import Dict, List


def grid_traveller(m: int, n: int, memo: List[List[int]] = None) -> int:
    # Recursive solution with n^n time complexity
    # if m < 1 or n < 1:
    #     return 0
    # if m == 1 and n == 1:
    #     return 1
    #     return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)
    if not memo:
        dim = max(m + 1, n + 1)
        memo = [[None] * dim for _ in range(dim)]
        for i in range(dim):
            memo[i][0] = 0
            memo[0][i] = 0
        memo[1][1] = 1
    if memo[m][n] is None:
        max_path = grid_traveller(m - 1, n, memo) + grid_traveller(m, n - 1, memo)
        memo[m][n] = max_path
        memo[n][m] = max_path
    return memo[m][n]


if __name__ == '__main__':
    # Iterative
    print(f"Grid Traveller Problem")
    print(f"grid_traveller(2, 3): {grid_traveller(2, 3)}")
    # print(f"grid_traveller(3, 2): {grid_traveller(3, 2)}")
    print(f"grid_traveller(3, 3): {grid_traveller(3, 3)}")
    print(f"grid_traveller(18, 18): {grid_traveller(18, 18)}")
