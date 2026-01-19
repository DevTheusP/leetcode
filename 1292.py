"""
Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 104
0 <= threshold <= 105
"""
from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])
        
        # Constrói a Prefix Sum Matrix 2D
        # P[i][j] representa a soma de todos os elementos no retângulo de (0,0) até (i-1, j-1)
        # O tamanho é (rows + 1) x (cols + 1) pra facilitar os casos de borda.
        P = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                # Soma = PrefixSum acima + PrefixSum esquerda - PrefixSum diagonal (interseção contada 2x) + valor atual
                P[r][c] = P[r-1][c] + P[r][c-1] - P[r-1][c-1] + mat[r-1][c-1]
        
        def get_rect_sum(r1, c1, r2, c2):
            # Calcula a soma do retângulo definido por:
            # - r1, c1: Linha/Coluna superior esquerda
            # - r2, c2: Linha/Coluna inferior direita
            return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]

        max_side = 0
        
        # Itera por cada célula da matriz tratando-a como o canto inferior direito de um possível quadrado
        for r in range(rows):
            for c in range(cols):
                # Tenta expandir o quadrado apenas se conseguir um tamanho maior que o atual (max_side + 1)
                # Verifica se é possível formar um quadrado de tamanho (max_side + 1) terminando em (r, c)
                # O canto superior esquerdo seria (r - max_side, c - max_side)
                
                if r >= max_side and c >= max_side:
                    # Verifica a soma desse novo quadrado candidato
                    current_sum = get_rect_sum(r - max_side, c - max_side, r, c)
                    
                    # Se a soma for válida, encontra um quadrado maior!
                    # Pode incrementar max_side.
                    # Não precisa diminuir max_side depois, pois prcisa só do MÁXIMO global.
                    if current_sum <= threshold:
                        max_side += 1
                        
        return max_side

