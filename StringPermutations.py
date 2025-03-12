class StringPermutations:
    def solve(self,s):
        ans = []
        chars = list(s)

        def recur(index,newS):
            if index==len(newS):
                ans.append("".join(newS))
                return

            for i in range(index,len(s)):
                newS[index], newS[i] = newS[i], newS[index]
                recur(index+1,newS)
                newS[index], newS[i] = newS[i], newS[index]

        recur(0,chars)
        ans.sort()
        return ans

    def main(self):
        s = "abc"
        print(self.solve(s))


perm = StringPermutations()
perm.main()