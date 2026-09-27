class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return not stack






"""
thought process: stack to keep track of most recent thing pushed 
if open brace, push
if closed brace, check most recent thing pushed, if matching pop and continue
--> if not matching, return false
"""

        