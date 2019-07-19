class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        r_a = a.split('+', 1)
        r_b = b.split('+', 1)
        r_num = int(r_a[0]) * int(r_b[0]) - int(r_a[1][:-1]) * int(r_b[1][:-1])
        img_num = int(r_a[0]) * int(r_b[1][:-1]) + int(r_a[1][:-1]) * int(r_b[0])
        return str(r_num) + "+" + str(img_num) + "i"


    

def main():  
    input = "1+-1i", "1+-1i"  
    ans = Solution().complexNumberMultiply("1+-1i", "1+-1i")
    print(ans)
if __name__ == "__main__":
    main()