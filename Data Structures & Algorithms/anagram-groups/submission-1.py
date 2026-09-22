class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # have an ouput array.
        # if output is empty push the word
        # check the first element of all array in output matches the word
        # push to that particular array it it matches
        # imeplement anagram seperate fuinction and call it.
        patterns = {}
        for each_str in strs:
            key = tuple(sorted(each_str))

            if key not in patterns:
                patterns[key] = []
            patterns[key].append(each_str)
        return list(patterns.values())




    def check_anagram(self, source: str, target: str) -> bool:
        if len(source) != len(target):
            return False
        s_count, t_count = {}, {}

        for ch in source:
            s_count[ch] = s_count.get(ch, 0) + 1
        
        for ch in target:
            t_count[ch] = t_count.get(ch, 0) + 1
        
        return s_count == t_count