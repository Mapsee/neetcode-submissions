class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hsh = {}
        for word in strs:
            arr = [0 for i in range(26)]
            for c in word:
                arr[ord(c) - ord('a')] += 1
            hsh[tuple(arr)] = hsh.get(tuple(arr), []) + [word]

        for k in hsh.keys():
            res.append(hsh[k])
        return res


        