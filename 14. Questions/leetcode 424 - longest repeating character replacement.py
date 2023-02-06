# longest repeating character replacement | leetcode 424 | https://leetcode.com/problems/longest-repeating-character-replacement/
# keep track of max freq in sliding window and check if size of window - max freq > k

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ptrL = 0
        ptrR = 0
        longest = 0
        freq = dict()
        max_freq = 0
        w_size = 0

        for ptrR in range(len(s)):
            freq[s[ptrR]] = 1 + freq.get(s[ptrR], 0)
            max_freq = max(max_freq, freq[s[ptrR]])

            if (ptrR - ptrL + 1) - max_freq > k:
                freq[s[ptrL]] -= 1
                ptrL += 1

            longest = max(longest, (ptrR - ptrL + 1))

        return longest