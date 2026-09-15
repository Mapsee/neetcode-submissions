class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_anagrams = defaultdict(list)

        for word in strs: 
            anagram_for_word = defaultdict(int)
            for c in word:
                anagram_for_word[c] += 1
            
            key = tuple(sorted(word))
            all_anagrams[key].append(word)
            # all_anagrams[key] = all_anagrams[key].append(word)
            # all_anagrams[key] = all_anagrams[key] + [word]
        
        res = []
        for list_of_words in all_anagrams.values():
            res.append(list_of_words)
        
        return res
                

            
            

                


        