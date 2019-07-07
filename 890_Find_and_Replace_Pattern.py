class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        for word in words:
            if self.wordmatch(word,pattern) is True:
                ans.append(word)
        return ans
    def wordmatch(self, word, pattern):
        tmp = {}
        for i in range(len(pattern)):
            if pattern[i] not in tmp:
                if word[i] in tmp.values():
                    return False
                else:
                    tmp[pattern[i]] = word[i]
            else:
                if tmp[pattern[i]] is not word[i]:
                    return False
        return True

def main():
    
    input = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"
    ans = Solution().findAndReplacePattern(input,pattern)
    print(ans)
if __name__ == "__main__":
    main()