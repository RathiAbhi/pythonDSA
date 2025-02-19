class PrefixSearch:
    """
    given a string and a prefix
    """
    def prefixSearch(self,word:str,prefix:str)->list[int]:
        ans = []
        n = len(prefix)
        i = 0
        while i<len(word)-n:
            if word[i:i+n]==prefix:
                ans.append(i)
                i += n
            else:
                i += 1

        return ans

    def main(self):
        if self.prefixSearch("GeeksforGeeks","Gee")==[0,8]:
            print("pass")
        else:
            print("fail")

search = PrefixSearch()
search.main()