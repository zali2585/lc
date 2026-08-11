class Solution:
    def checkValidString(self, s: str) -> bool:
        # high = max amount of open paran there can be (ie, every star is interpreted as open paran)
        # use: if this ever dips below 0, then u know this isnt a valid paran string bc it means at that point of the string, even after interpreting every * as open, the amount of closed paran outmatch open parans so u cant properly match
        # ex: (*))) [by last close paran, even if u interpret * as open paran, balance = open - close or 2 - 3, negative, and u can see that theres never gonna be enough open parans before that closed paran to match ]
        high = 0
        # low = min amount of open paran there can be (every star interpreted as closed paran)
        # use: if low drops below 0, then u interpreted one too many stars as closed, so u reset to interpret one as empty each char check
        low = 0
        for c in s:
            if c == '(':
                high += 1
                low += 1
            elif c == ')':
                high -= 1
                low -= 1
            else:
                high += 1
                low -= 1
            
            if high < 0:
                return False
            low = max(low, 0)
        # if low == 0, then open = closed and theres never a point in string where close outweighs open [ie, looks like ())] or else wouldve returned early with high
        # additionally, correct amount of * interpreted as empty and closed
        return low == 0
            

        