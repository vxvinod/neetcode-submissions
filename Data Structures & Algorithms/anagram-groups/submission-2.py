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

