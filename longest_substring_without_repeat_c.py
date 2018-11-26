
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp=s[0]
        tmp1=""
        result={}
        for i in range(1,len(s)):
            if tmp.find(s[i])!=-1:
                if tmp1!="" :
                    if len(tmp1)>len(tmp2):
                        tmp1=tmp
                    else:
                        
                tmp1=tmp
                tmp=""
            else:
                tmp+=s[i]
        print(tmp)
        print(tmp1)

        

def main():
    s=Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print("---")
    print(s.lengthOfLongestSubstring("bbbbb"))
    print("---")
    print(s.lengthOfLongestSubstring("pwwkew"))

if __name__ == '__main__':
    main()         
