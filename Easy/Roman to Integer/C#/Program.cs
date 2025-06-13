public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char, int> conversion = new Dictionary<char, int> {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int response = 0;
        for (int i = 0; i < s.Length -1; i++)
        {
            if (conversion[s[i]] < conversion[s[i+1]]) {
                response -= conversion[s[i]];
            } else {
                response += conversion[s[i]];
            }
        }

        response += conversion[s[s.Length - 1]];
        return response;
    }
}