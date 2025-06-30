public class Solution
{
    public bool IsValid(string s)
    {
        Stack<char> stack = new Stack<char>();
        Dictionary<char, char> pairs = new Dictionary<char, char>
        {
            {')','('},
            {'}', '{'},
            {']', '['}
        };

        foreach (char item in s)
        {
            if (pairs.ContainsKey(item))
            {
                if (stack.Count == 0 || stack.Pop() != pairs[item])
                {
                    return false;
                }
            }
            else
            {
                stack.Push(item);
            }
        }
        return stack.Count == 0;
    }
}