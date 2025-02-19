import sys

class LongestUniformSubstring:
    """
    given a string, we have to return the longest substring with same characters
    the return list contains the index from where it starts repeating and the length
    """
    def longestSubstring(self,s:str)-> list[int]:
        if len(s)==1:
            return [0,1]

        left,right = 0,0
        ans = [0,1]

        while right<len(s):
            if s[right]==s[left]:
                if (right-left+1)>ans[1]:
                    ans = [left,right-left+1]
            else:
                left = right

            right += 1
        return ans

    def main(self):
        if (self.longestSubstring("aaBBcccc")==[4,4] and
        self.longestSubstring("abbbccda")==[1,3] and
        self.longestSubstring("aabbbbbCdAA")==[2,5] and
        self.longestSubstring("10000111")==[1,4]):
            print("pass")
        else:
            print("fail")

longstring = LongestUniformSubstring()
longstring.main()