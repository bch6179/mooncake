﻿For hard, only read diagram
For solving first and then optim
#reverse trangle DP, combined DP
f[i] min number of cuts need for s[i:n] for every sub be palindrome abb ,   new+sufix, new is s[i:j], if new is true, then result DPi = DPj+1, 
Init f[i] = n-i - 1, i in range(n+1), f[n] = -1, last return f[0] 
f[i] = min { f([j]+1} where j > i and j+1 : i is palindrome 
  if s[i] == s[j] and (j-i <2 or dp[i+1][j-1])
     f[i] = min(f[i], f[j]+1)
*#
 * #
  * #  for i in range(n)
    *   for j in range i,n
   
   f[i] either for cut results(mincut+1), then rturn result-1 or just cut number
   for i in reversed(range(n)):
   
#Regular

find isPalindrome metrics first, and DP
 
state: f[i]”前i”个字符组成的子字符串需要最少 几次cut(最少能被分割为多少个字符串-1) function: f[i] = MIN{f[j]+1}, j < i && j+1 ~ i这一 段是一个回文串 intialize: f[i] = i - 1 (f[0] = -1) answer: f[s.length()]


#
    def dfs(self, s, pos,  cut):
        if pos == len(s)-1:
            self.res = min(self.res, cut)
            return
        for i in range(pos+1, len(s)):
            if self.isPalindrome(s[pos:i]):
                self.dfs(s, i, cut+1)
                
 prune: 
 memory [pos, cut], a a bb [a a] bb