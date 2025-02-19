import sys


class DistanceBetweenStrings:
    def distanceBetweenStrings(self, document:str, word1:str, word2:str)->int:
        words = document.lower().split()

        currentWordIndex = 0
        wordOneMidPointIndex = 0
        wordTwoMidPointIndex = 0

        shortDist = sys.maxsize

        for word in words:
            if word==word1:
                wordOneMidPointIndex = currentWordIndex + len(word1)/2
            elif word==word2:
                wordTwoMidPointIndex = currentWordIndex + len(word2)/2

            if wordOneMidPointIndex>0 and wordTwoMidPointIndex>0:
                shortDist = min(shortDist, abs(wordTwoMidPointIndex-wordOneMidPointIndex))

            currentWordIndex += len(word)+1 #assuming there would have been 1 space between the words

        print(word1,word2,shortDist)
        return shortDist

    def main(self):
        document = "In publishing and graphic design, lorem ipsum is a filler text commonly used to demonstrate the graphic elements lorem ipsum text has been used in typesetting since the 1960s or earlier, when it was popularized by advertisements for Letraset transfer sheets. It was introduced to the Information Age in the mid-1980s by Aldus Corporation, which"
        if (self.distanceBetweenStrings(document, "and","graphic")==6 and
        self.distanceBetweenStrings(document,"transfer","it")==14):
            print("Pass")
        else:
            print("Fail")

dis = DistanceBetweenStrings()
dis.main()