# state: f[i]代表我跳到这个位置最少需要几步 function: f[i] = MIN(f[j]+1, j < i && j能够跳到i) initialize: f[0] = 0; answer: f[n-1]
      # 3  3  0 2 5 7 8 9
        #   start   lend gend 
        #from DP, conduction if j+a[j] >= i, then it must true for any k < i;hence no need check following j
        #also not overlapping problem, it's linear with index, only the key points matter, instead of an array of DP
        #use minStep which only change after some window shift; use maxReach for the cover
        # this is just greedy, jump the farthest in current phase(window), in each index, get the max next coverage
        # optimze from DP,for case of 2 3 1 1 1
        #                             _____ 
        #                                   ____
        # w1 or edge1 = nums[0] cover what first jump reach , so minstep+=1, FOR each i,compute MR
        # after i > edge1, go to next jump window, update cover edge2 = next MR  
