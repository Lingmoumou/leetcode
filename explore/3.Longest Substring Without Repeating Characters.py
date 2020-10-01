
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        :type s: str
        :rtype: int
        """
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength

        

def main():
    s=Solution()
    print(s.lengthOfLongestSubstring("abcabcbb")) # 3
    print("---")
    print(s.lengthOfLongestSubstring("bbbbb")) # 1
    print("---")
    print(s.lengthOfLongestSubstring("pwwkew")) # 3
    print("---")
    print(s.lengthOfLongestSubstring(" ")) # 1
    print("---")
    print(s.lengthOfLongestSubstring("aab")) # 2
    print("---")
    print(s.lengthOfLongestSubstring("dvdf")) # 3
    print("---")
    print(s.lengthOfLongestSubstring("tmmzuxt")) # 5
    print("---")
    print(s.lengthOfLongestSubstring("jbpnbwwd")) # 4
    print("---")
    print(s.lengthOfLongestSubstring("wobgrovw")) # 6
    print("---")
    print(s.lengthOfLongestSubstring("kdgjkjhglfp")) # 7
    print("---")
    print(s.lengthOfLongestSubstring("uqinntq")) # 4
    print("---")
    print(s.lengthOfLongestSubstring("kdgjkjhglfp")) # 7

    
    

if __name__ == '__main__':
    main()         
