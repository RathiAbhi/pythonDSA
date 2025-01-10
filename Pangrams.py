class Pangrams:
    """
    a string that has all the characters from alphabets is called a pangram
    we need to check if the given string is a pangram and also need
    to return the missing characters as a string if in case it's not
    """
    def pangrams(self, s: str)->str:
        Alphabet = "abcdefghijklmnopqrstuvwxyz"
        s = s.lower()
        res = ""
        for char in Alphabet:
            if char not in s:
                res += char

        print(res)
        return res

    def main(self):
        if (self.pangrams("The quic brown for jumps over the lazy dog")=="kx" and
        self.pangrams("abcdefghijklmnopqrstuvwxyz")=="" and
        self.pangrams("")=="abcdefghijklmnopqrstuvwxyz"):
            print("Pass")
        else:
            print("fail")

pang = Pangrams()
pang.main()