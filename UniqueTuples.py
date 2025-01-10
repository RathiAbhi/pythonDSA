class UniqueTuples:
    """
    given a string, return all the unique tuples of a given length
    """

    def uniqueTuples(self,s:str,length:int):
        result = set()

        for i in range(len(s)-length+1):
            result.add(s[i:i+length])

        return result

    def main(self):
        print(self.uniqueTuples("aab",2))
        print(self.uniqueTuples("abbccde",2))

tuples = UniqueTuples()
tuples.main()