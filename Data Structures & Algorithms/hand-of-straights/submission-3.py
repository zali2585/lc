# this is greedy bc by taking the smallest card each time, it forces u build the group x + 1, x + 2 ... x + groupSize - 1
# there is ordering constraint, and using consistently smallest card is necessary
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        hand.sort()

        for start in hand:
            if count[start] == 0:
                continue
            
            for card in range(start, start + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1
        return True