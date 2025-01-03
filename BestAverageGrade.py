class BestAverageGrade:
    """
    Problem: Given a list of student test scores, find the best average grade. Each student may have more than one test score in the list.
    Logic: traverse each name & marks using a loop
    and maintain two maps for score and frequency
    Each time a new entry comes, update the score and frequency of that student
    and then calculate the avg
    In the end, compare the avg with max avg so far and return it at loop exit
    """
    def bestAverageGrade(self,Input)-> int:
        score = {}
        freq = {}
        maxAvg = 0
        for name, marks in Input:
            score[name] = score.get(name,0) + int(marks)
            freq[name] = freq.get(name,0) + 1
            maxAvg = max(maxAvg, score[name]/freq[name])

        return int(maxAvg)

    def main(self):
        Input =  [["Bob", "87"], ["Mike", "35"], ["Bob", "52"], ["Jason", "35"], ["Mike", "55"], ["Jessica", "99"]]
        print(self.bestAverageGrade(Input))

bestGrade = BestAverageGrade()
bestGrade.main()