class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        res = 0
        maxF = 0
        for r, c in enumerate(s):
            freq[c] += 1
            maxF = max(maxF, freq[c])
            while r - l + 1 - maxF > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res