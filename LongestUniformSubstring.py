import sys


class LongestUniformSubstring:
    """
    given a string, we have to return the longest substring with same characters
    the return list contains the index from where it starts repeating and the length
    """
    def longestSubstring(self,s:str)-> list[int]:
        if len(s)==1:
            return [0,1]

        ans = [0,1]
        maxCount = -sys.maxsize
        count = 1
        index = 0

        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count += 1
            else:
                if count > maxCount:
                    maxCount = count
                    ans[0] = index
                    ans[1] = maxCount
                    index = i
                count = 1

        if count > maxCount:
            ans[0] = len(s) - count
            ans[1] = count

        print(ans)
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
