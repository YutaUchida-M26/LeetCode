#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True]
        for i in range(1,len(s)+1):
            for j in wordDict:
                if i >= len(j) and s[i-len(j):i] == j and dp[i-len(j)] == True:
                    dp.append(True)
                    break
            if len(dp) <= i:
                dp.append(False)
        return dp[-1]
# @lc code=end

