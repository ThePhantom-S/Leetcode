class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mp = {'a':-1,'b':-1,'c':-1}
        count = 0
        
        for i, char in enumerate(s):
            mp[char] = i
            min_index = min(mp['a'],mp['b'],mp['c'])
            if min_index!=-1:
                count += (min_index+1)
        return count


