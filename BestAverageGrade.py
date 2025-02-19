import sys


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
        marks = {}
        freq = {}
        maxAvg = float('-inf')

        for name,mark in Input:
            mark = int(mark)
            marks[name] = marks.get(name,0)+mark
            freq[name] = freq.get(name,0)+1

        for name in marks:
            avg = marks[name]/freq[name]
            maxAvg = max(avg,maxAvg)

        return int(maxAvg)

    def main(self):
        Input =  [["Bob", "87"], ["Mike", "35"], ["Bob", "52"], ["Jason", "35"], ["Mike", "55"], ["Jessica", "99"]]
        print(self.bestAverageGrade(Input))

bestGrade = BestAverageGrade()
bestGrade.main()