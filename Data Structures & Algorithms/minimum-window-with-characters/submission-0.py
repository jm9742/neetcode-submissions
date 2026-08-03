class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s and not t:
            return ""

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1
        
        required = len(need)
        have = 0

        best_length = float("inf")
        best_left = 0
        best_right = 0

        window = {}
        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == required:
                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right

                left_char = s[left]
                window[left_char] -= 1

                if (
                    left_char in need
                    and window[left_char] < need[left_char]
                ): have -= 1

                left += 1
        
        if best_length == float('inf'):
            return ""
        
        return s[best_left : best_right+1]


        