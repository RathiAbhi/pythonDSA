class FirstNonRepeatingCharacter:
    def firstNonRepeatingCharacter(self,s:str)->int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char,0)+1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1

    def main(self):
        input = ["leetcode", "apple", "racecars", "aabb"]
        output = [0,0,3,-1]

        for i in range(len(input)):
            if (self.firstNonRepeatingCharacter(input[i])!=output[i]):
                print("Fail")
                break

        print("Pass")

character = FirstNonRepeatingCharacter()
character.main()