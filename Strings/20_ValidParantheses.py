class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in closed:
                stack.pop() if stack and stack[-1] == closed[i] else False
            else:
                stack.append(i)

        return True if not stack else False


solution = Solution()
solution.isValid("([)]")
