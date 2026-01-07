from typing import Optional

"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

Constraints:
The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Calcula o produto máximo ao dividir a árvore binária em duas subárvores.
        
        Lógica:
        1 Primeiro, calcula a soma total de todos os nós da árvore (total_sum).
        2 Enquanto faz isso (usando uma travessia pós-ordem/DFS), armazena a soma de cada subárvore encontrada.
        3 Para dividir a árvore em duas, corta a aresta acima de qualquer nó. 
           Se a soma da subárvore desse nó for 's', então a soma da outra parte da árvore será 'total_sum - s'.
        4 O produto das duas partes será s * (total_sum - s).
        5 Itera sobre todas as somas de subárvores encontradas para achar o produto máximo.
        6 Retorna o resultado módulo 10^9 + 7.
        """
        all_sums = []

        def tree_sum(node):
            if not node:
                return 0
            # Calcula a soma da subárvore atual repetindo o processo para a esquerda e direita
            current_sum = node.val + tree_sum(node.left) + tree_sum(node.right)
            all_sums.append(current_sum)
            return current_sum

        # Passo 1: Calcular a soma total da árvore e preencher all_sums
        total_sum = tree_sum(root)
        
        # Passo 2: Encontrar o produto máximo
        max_p = 0
        for s in all_sums:
            # O produto é a soma da subárvore atual * soma do restante da árvore
            current_product = s * (total_sum - s)
            if current_product > max_p:
                max_p = current_product
        
        # Passo 3: Retorna com módulo
        return max_p % (10**9 + 7)