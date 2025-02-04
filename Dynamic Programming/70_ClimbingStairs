import functools

class Solution:
    @functools.cache # will get TLE without memoization
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
solution = Solution()
solution.climbStairs(n = 2)