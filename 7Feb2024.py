class Solution:
    def frequencySort(self, s: str) -> str:
        def idx(c):
            if c >= 'a':
                return ord(c) - ord('a') + 36
            if c >= 'A':
                return ord(c) - ord('A') + 10
            return ord(c) - ord('0')

        def toChar(i):
            # print(i)
            if i >= 36:
                return chr(i - 36 + ord('a'))
            if i >= 10:
                return chr(i - 10 + ord('A'))
            return chr(i + ord('0'))

        fre = [[0, i] for i in range(62)]
        for char in s:
            fre[idx(char)][0] += 1
        fre.sort(key=lambda x: (-x[0], x[1]))
        result = ""
        for freq, index in fre:
            # print(freq,index,toChar(5))
            result += toChar(index)*freq
        return result