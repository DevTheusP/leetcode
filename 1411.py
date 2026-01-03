"""
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.
"""

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Two types of patterns for a row:
        # 1. ABA (2 colors): e.g., R-Y-R. Initial ways: 6
        # 2. ABC (3 colors): e.g., R-Y-G. Initial ways: 6
        aba = 6
        abc = 6
        
        # Transitions based on previous row type:
        # ABA -> 3 * ABA + 2 * ABC
        # ABC -> 2 * ABA + 2 * ABC
        for _ in range(n - 1):
            new_aba = (3 * aba + 2 * abc) % MOD
            new_abc = (2 * aba + 2 * abc) % MOD
            aba, abc = new_aba, new_abc
            
        return (aba + abc) % MOD