"""
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted multiple times.

 

Example 1:

Input: squares = [[0,0,1],[2,2,1]]

Output: 1.00000
"""

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Calcula a área total de todos os quadrados
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2.0
        
        # Define o intervalo de busca para a coordenada Y
        # O menor Y possível é o menor 'y' de todos os quadrados
        # O maior Y possível é o maior 'y + l' (topo) de todos os quadrados
        min_y = min(y for _, y, _ in squares)
        max_y = max(y + l for _, y, l in squares)
        
        low = min_y
        high = max_y
        
        # Binary Search para encontrar o Y onde a área abaixo é igual a metade da área total
        # Como é um valor contínuo (float), executa por um número fixo de iterações
        # 100 iterações são suficientes para atingir a precisão de 10^-5
        for _ in range(100):
            mid = (low + high) / 2
            current_area_below = 0
            
            for _, y, l in squares:
                # Se o quadrado está totalmente abaixo da linha 'mid'
                if y + l <= mid:
                    current_area_below += l * l
                # Se o quadrado está totalmente acima da linha 'mid'
                elif y >= mid:
                    continue
                # Se a linha 'mid' corta o quadrado
                else:
                    # A parte abaixo da linha é altura (mid - y) * largura (l)
                    current_area_below += (mid - y) * l
            
            # Se a área abaixo for maior ou igual ao alvo, precisa diminuir o Y (tentar mais baixo)
            # ou seja, a resposta está na metade inferior
            if current_area_below >= target:
                high = mid
            else:
                low = mid
                
        return high
        