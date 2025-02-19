
"""A group of students sitting in a circle, the teacher wants to elect the class monitor.
The teacher sings a song and goes around the students, whichever student the song ends at
that is eliminated. The elimination continues and remaining is class monitor.

n - students
k - length

after every round, n = n - (n//k)
"""

class Election:
    def monitor(self,n,k):
        arr = list(range(1,n+1))
        index = 0

        while len(arr)>1:
            index = (index+k-1)%len(arr)
            arr.pop(index)

        return arr[0]

    def optimizedMonitor(self,n,k):
        index = 1
        ans = 0
        while index<=n:
            ans = (ans + k)%index
            index += 1

        return ans + 1

    def main(self):
        print(self.monitor(12,3))
        print(self.optimizedMonitor(12,3))

elect = Election()
elect.main()