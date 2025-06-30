class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # to store the open parentheses
        pairs = {')': '(', '}': '{', ']': '['} # associate close parentheses to the correspondant open parentheses

        for char in s:
            if char in pairs: # verify if char is close parenthese
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return not stack