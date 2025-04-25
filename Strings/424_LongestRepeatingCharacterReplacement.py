class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        result = 0
        freq = 0

        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            freq = max(freq, count[s[right]])

            if (right - left + 1) - freq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result


solution = Solution()
solution.characterReplacement("AABABBA", 1)
