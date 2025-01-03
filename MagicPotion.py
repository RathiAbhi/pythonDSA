class MagicPotion:
    """
    Combine ingredients in a specific order, any of which may be repeated

    As an example, consider the following
    (A,B,C,D) in 11 steps: A, B, A, B, C, A, B, A, B, C, E

    Encode the string above using only 6 characters: A,B,*,C,*,E

    Implement function that takes as input an un-encoded potion and returns the
    minimum number of characters required to encode


    Logic: initialize an empty string
    go through ingredients character by character
    form two substrings one ending at that character, and one of similar length in the remaining part
    if they are similar,then add * to the initialized string otherwise add the character
    return the initialized string's length
    """

    def minimalSteps(self, ingredients: str) -> int:
        print(f"The input is {ingredients}")
        n = len(ingredients)
        if n==0:
            return 0

        magicPotion = ""
        magicPotion += ingredients[0]
        i=1
        while i<n:
            if (i*2<=n):
                stringToCompare = ingredients[:i]
                remaining = ingredients[i:2*i]

                if stringToCompare==remaining:
                    magicPotion += '*'
                    i = i*2
                else:
                    magicPotion += ingredients[i]
                    i +=1
            else:
                magicPotion += ingredients[i]
                i +=1
        print(magicPotion)
        return len(magicPotion)


    def main(self):
        if (self.minimalSteps("ABABCABABCE") == 6 and self.minimalSteps("ABCDABCE") == 8
                and self.minimalSteps("ABCABCE") == 5 and self.minimalSteps("AAA") == 3
                and self.minimalSteps("AAAA") == 3 and self.minimalSteps("BBB") == 3
                and self.minimalSteps("AAAAAAAA") == 4):
            print("Pass")
        else:
            print("Fail")

potion = MagicPotion()
potion.main()