from typing import List

height = [4, 3, 2, 1, 4]


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        print(area)
        return area


solution = Solution()
solution.maxArea(height)
