# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()
        print(deck)
        ans = [0 for _ in range(len(deck))]
        q = deque([i for i in range(len(deck))])

        i = 0
        while len(q) > 1:
            top = q.popleft()
            next_top = q.popleft()
            # print(top)
            ans[top] = deck[i]
            q.append(next_top)
            i += 1
        
        top = q.popleft()
        ans[top] = deck[i]

        return ans

        pass