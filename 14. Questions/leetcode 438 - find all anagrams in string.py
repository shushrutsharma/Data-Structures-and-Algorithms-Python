# find all anagrams in string | leetcode 438 | https://leetcode.com/problems/find-all-anagrams-in-a-string/
# sliding window to track "which" substring; add ptr2 to counter, remove ptr1 from counter


from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        Ns, Np = len(s), len(p)
        ptr1 = 0
        ptr2 = Np - 1
        anagrams = []
        freq_s, freq_p = Counter(s[ptr1:(ptr2 + 1)]), Counter(p)

        while ptr2 < Ns:
            if freq_s == freq_p:
                anagrams.append(ptr1)
            freq_s[s[ptr1]] -= 1
            ptr1 += 1
            ptr2 += 1
            if ptr2 != Ns:
                freq_s[s[ptr2]] = 1 + freq_s.get(s[ptr2], 0)

        return anagrams