class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        tree_level = 0
        inverse = True
        tmp = label
        zigzag = []
        while True:
            if label < pow(2,tree_level):
                tree_level -= 1
                zigzag.append(tmp)
                
                while tree_level > 1:                    
                    if tmp % 2 == 0:
                        tmp /= 2
                    else:
                        tmp = (tmp - 1)/2
                    if inverse is True:
                        zigzag.append(int(pow(2,tree_level) - 1 - tmp + pow(2,tree_level-1)))
                        inverse = False
                    else:
                        zigzag.append(int(tmp))
                        inverse = True
                    tree_level -= 1
                zigzag.append(1)
                zigzag.reverse()
                return  zigzag           
            tree_level += 1
def main():  
    input = 26
    ans = Solution().pathInZigZagTree(input)
    print(ans)
if __name__ == "__main__":
    main()