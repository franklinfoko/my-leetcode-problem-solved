class Solution:
    def romanToInt(self, s: str) -> int:
        # XIX
        val_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        #s_list = list(s)
        r = 0
        for i in range(len(s) -1):
            if val_dict[s[i]] < val_dict[s[i+1]] :
                r -= val_dict[s[i]]
            else:
                r += val_dict[s[i]]
        r += val_dict[s[-1]] 
        return r