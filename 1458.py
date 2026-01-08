from typing import List

"""
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

 

Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.
Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.
Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.
 

Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000
"""

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # Esse aqui eu usei i.a pra ajudar, nao sabia resolver sozinho
        
        n, m = len(nums1), len(nums2)
        
        # dp[i][j] vai guardar o produto escalar máximo considerando nums1[0...i] e nums2[0...j]
        # Inicializamos com -infinito
        dp = [[float('-inf')] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                # Calcula o produto dos elementos atuais
                product = nums1[i] * nums2[j]
                
                # Usa o par (nums1[i], nums2[j])
                # Pode estender uma subsequência anterior vinda de dp[i-1][j-1]
                # Se dp[i-1][j-1] for negativo, é melhor começar uma nova subsequência apenas com 'product'
                # Por isso usa max(0, prev_diag)
                prev_diag = dp[i-1][j-1] if (i > 0 and j > 0) else 0
                term_with_current = product + max(0, prev_diag)
                
                # Pula nums1[i] (herda o melhor resultado de cima)
                prev_up = dp[i-1][j] if i > 0 else float('-inf')
                
                # Pula nums2[j] (herda o melhor resultado da esquerda)
                prev_left = dp[i][j-1] if j > 0 else float('-inf')
                
                # O valor para o estado atual é o melhor dentre:
                # - Usar o par atual (estendendo ou não)
                # - Pula nums1[i]
                # - Pula nums2[j]
                dp[i][j] = max(term_with_current, prev_up, prev_left)
                
        # O resultado final tá na última célula
        return int(dp[n-1][m-1])