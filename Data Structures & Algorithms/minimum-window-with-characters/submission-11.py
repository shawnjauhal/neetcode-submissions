class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countsT = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            countsT[c] += 1
        need = len(countsT)
        have = 0
        res = [-1, -1]
        resLen = math.inf
        l = 0
        for r, c in enumerate(s):
            window[c] += 1
            if c in countsT and window[c] == countsT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countsT and window[s[l]] < countsT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != math.inf else ""
