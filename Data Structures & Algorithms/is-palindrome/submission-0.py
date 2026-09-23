class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_palindrome = True
        filtered = [ch for ch in s.lower() if ch.isalnum()]
        filt_len = len(filtered)
        for i in range(filt_len//2):
            if filtered[i] != filtered[filt_len-i-1]:
                return False
        return True