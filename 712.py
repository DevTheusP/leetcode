"""
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
3. Matriz Final
Visualmente, a matriz dp ficou assim:

(vazio)	e	a	t
(vazio)	0	0	0	0
s	0	0	0	0
e	0	101	101	101
a	0	101	198	198
O valor no canto inferior direito (dp[3][3]) é 198. Isso significa que a maior soma ASCII comum entre "sea" e "eat" é 198 (que corresponde às letras "ea").
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # Cria uma matriz dp com m+1 linhas e n+1 colunas, todas inicializadas com zero
        dp = []
        for _ in range(m + 1):
            row = [0] * (n + 1)
            dp.append(row)
        
        # Preenche a matriz dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Calcula a soma total de ASCII de ambas as strings
        total_ascii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        
        # Retorna a soma total menos duas vezes a maior soma comum
        return total_ascii - 2 * dp[m][n]
        
                    