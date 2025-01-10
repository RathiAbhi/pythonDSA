class ReverseString:
    """
    given a string, return the reversed string
    """
    def reverseString(self,word:str)->str:
        chars = [char for char in word]
        chars.reverse()
        return "".join(chars)

    def main(self):
        if self.reverseString("abcd")=="dcba":
            print("pass")
        else:
            print("fail")

reverse = ReverseString()
reverse.main()