class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        d = defaultdict(int)

        for i in hand:
            d[i] += 1 
        hand.sort()
        for temp in hand:
            if d[temp]:
                for i in range(temp, temp + groupSize ):
                    if not d[i]:
                        return False
                    d[i] -=1
        return True