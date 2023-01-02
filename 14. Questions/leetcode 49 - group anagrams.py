# group anagrams | leetcode 49 | https://leetcode.com/problems/group-anagrams/
# method: dictionary with char counter as key

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        grouped = defaultdict(list)
        
        for each_word in strs:
            count_of_ch = [0] * 26
            for each_ch in each_word:
                count_of_ch[ord(each_ch) - ord("a")] += 1
            grouped[tuple(count_of_ch)].append(each_word)
            
        return grouped.values()
