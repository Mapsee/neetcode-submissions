class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            hsh[sorted_word] = hsh.get(sorted_word, []) + [word]

        res = []
        for k in hsh.keys():
            res.append(hsh[k])
        
        return res

        
        