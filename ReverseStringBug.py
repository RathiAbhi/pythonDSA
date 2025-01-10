class ReverseStringBug:
    """
    given a string, reverse the order of words without reversing the words
    and the words are separated by dots, also there might be test cases which
    have leading and trailing dots
    "i.like.this.program.very.much" --> "much.very.program.this.like.i"
    """
    def reverseString(self,s:str)->str:
        words = s.split('.')
        words.reverse()
        return '.'.join(words)

    def main(self):
        if self.reverseString("i.like.this.program.very.much")=="much.very.program.this.like.i":
            print("pass")
        else:
            print("fail")

reverse = ReverseStringBug()
reverse.main()