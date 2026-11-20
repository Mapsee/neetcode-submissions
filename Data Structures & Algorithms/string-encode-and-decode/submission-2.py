class Solution:

    def encode(self, strs: List[str]) -> str:
        words = ''
        d = ''
        for word in strs:
            count = len(word)
            d = d + str(count) + '\\'
            words += word

        res = d + '#' + words
        return res

    def decode(self, s: str) -> List[str]:
        word_count = []
        to_splice = 0

        temp_count = ''
        for char in s:
            to_splice += 1
            if char == '\\':
                word_count.append(int(temp_count))
                temp_count = ''
            elif char == '#':
                break
            else:
                temp_count += char

        spliced_s = s[to_splice: len(s)]

        res = []
        for count in word_count:
            i = 0
            word = ''
            while i < count:
                word += spliced_s[i]
                i += 1
            res.append(word)
            spliced_s = spliced_s[i: len(spliced_s)]
        
        return res

            
            
