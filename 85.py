"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
"""
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # Para cada linha, atualiza o histograma de alturas
            for i, val in enumerate(row):
                if val == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # Agora calcula a maior área possível nesse histograma
            # Usa uma pilha para guardar os índices das colunas onde a altura está crescendo
            stack = [] 
            
            # Vou até cols + 1 para forçar o cálculo final (com altura 0)
            for i in range(cols + 1):
                current_h = heights[i] if i < cols else 0
                
                # Enquanto a altura atual for menor que a do topo da pilha,
                # sei que não posso estender aquele retângulo para a direita.
                # Então, fecha aquele retângulo e calcula sua área.
                while stack and current_h < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                
                stack.append(i)
                
        return max_area