from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Dicionário para armazenar a soma de cada nível
        level_sums = defaultdict(int) 
        
        # Stack para DFS: armazena tuplas (node, level)
        stack = [(root, 1)]
        
        while stack:
            node, level = stack.pop()
            
            # Adiciona o valor do nó atual à soma do seu nível
            level_sums[level] += node.val
            
            # Adiciona filhos à pilha (DFS)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        
        # Encontra o nível com a soma máxima
        max_sum = float('-inf')
        max_level = 1
        
        # Percorre os níveis ordenados para garantir que retornamos o menor índice em caso de empate
        for level in sorted(level_sums.keys()):
            if level_sums[level] > max_sum:
                max_sum = level_sums[level]
                max_level = level
                
        return max_level