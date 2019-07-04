class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse=True)
        reveal = []
        for num in deck:
            if len(reveal) > 1:
                tmp_pop = reveal.pop()
                reveal.insert(0,tmp_pop)
            reveal.insert(0,num)
        return reveal
def main():
    
    input = [17,13,11,2,3,5,7]
    
    
    ans = Solution().deckRevealedIncreasing(input)
    print(ans)
if __name__ == "__main__":
    main()