"""
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 

Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105
"""

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0
        min_abs_val = float('inf')
        
        for row in matrix:
            for val in row:
                # Somamos o valor absoluto de todos os elementos
                total_sum += abs(val)
                
                # Contamos quantos números negativos existem
                if val < 0:
                    negative_count += 1
                
                # Mantemos o rastreio do menor valor absoluto encontrado
                min_abs_val = min(min_abs_val, abs(val))
        
        # Lógica:
        # A operação permite multiplicar dois adjacentes por -1.
        # Isso significa que podemos "mover" um sinal negativo pela matriz.
        # Se tivermos dois negativos, podemos juntá-los e cancelá-los ((-1 * -1) = 1).
        # Portanto, se a quantidade de negativos for PAR, podemos tornar TODOS positivos.
        if negative_count % 2 == 0:
            return total_sum
        
        # Se a quantidade for ÍMPAR, sobrará inevitavelmente UM número negativo.
        # Para maximizar a soma, queremos que esse negativo seja o menor valor absoluto possível.
        # Como já somamos tudo como positivo em `total_sum`, precisamos subtrair esse valor duas vezes:
        # Uma vez para remover sua contribuição positiva, e outra para adicionar sua contribuição negativa.
        else:
            return total_sum - (2 * min_abs_val)
        