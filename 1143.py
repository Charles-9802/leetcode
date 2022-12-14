# 最长公共子序列，不连续
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])        # 不连续
            print(dp)
        return dp[-1][-1]

def main():
    text1 = "abcde"
    text2 = "ace"
    A = Solution()
    print(A.longestCommonSubsequence(text1, text2))


if __name__ == "__main__":
    main()
