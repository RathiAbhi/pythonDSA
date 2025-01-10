class RunLengthEncoding:
    """
    given a string, return its encoding
    aabbbccd -> a2b3c2d1
    """
    def encoding(self,s:str)->str:
        res = ""
        n = len(s)
        res += s[0]
        count = 1
        for i in range(1,n):
            if s[i]==s[i-1]:
                count += 1
            else:
                res += str(count)
                res += s[i]
                count = 1

        if count>0:
            res += str(count)

        return res

    def main(self):
        if self.encoding("aabbbccd")=="a2b3c2d1":
            print("pass")
        else:
            print("fail")

run = RunLengthEncoding()
run.main()