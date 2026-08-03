class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = {}
        count_s2 = {}

        for char in s1:
            count_s1[char] = count_s1.get(char, 0)+1
        
        left = 0

        for right in range(len(s2)):
            count_s2[s2[right]] = count_s2.get(s2[right], 0)+1
            if right - left + 1 > len(s1):
                left_char = s2[left]
                count_s2[left_char] -= 1
                if count_s2[left_char] == 0:
                    del count_s2[left_char]
                left += 1
            if count_s1 == count_s2:
                return True
        return False



           