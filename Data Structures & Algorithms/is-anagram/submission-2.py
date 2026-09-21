class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = None
        s_count = {}
        t_count = {}
        if len(s) != len(t):
            return False

        for ch in s:
            if ch not in s_count:
                s_count[ch] = 1
            else:
                s_count[ch] = s_count.get(ch, 0) + 1
        
        for ch in t:
            if ch not in t_count:
                t_count[ch] = 1
            else:
                t_count[ch] = t_count.get(ch, 0) + 1
        
        # for ch in s:
        #     if ch not in t:
        #         is_anagram = False
        
        return True if s_count == t_count else False
