 state: f[i][j] for first i strings at least  edition to become first j of B
  • function: f[i][j] = MIN(f[i-1][j]+1, f[i][j-1]+1, f[i-1][j-1])    // A[i - 1] == B[j - 1] 
  •                   = MIN(f[i-1][j]+1, f[i][j-1]+1, f[i-1][j-1]+1) // A[i - 1] != B[j - 1] 
  • initialize: f[i][0] = i, f[0][j] = j • answer: f[n][m]

Longest Common Subsequence
state: f[i][j] max length first i matching to the first j• function: f[i][j] = MAX(f[i-1][j], f[i][j-1], f[i-1][j-1] + 1) // A[i - 1] == B[j - 1] •                     = MAX(f[i-1][j], f[i][j-1])                         // A[i - 1] != B[j - 1] • intialize: f[i][0] = 0 f[0][j] = 0 • answer: f[n][m]
• Related Question: • http://www.lintcode.com/problem/longest-common-substring/
➨19页

为ொ஄᫝i-1? Aⓗ➨i୭Ꮠ➢ⓗ᫝A[i-1]