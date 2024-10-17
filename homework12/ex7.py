class AltermatingSums:
    def __init__(self,a):
        self.a = a
    def alternating_sums(self):
        team1 = sum(self.a[i] for i in range(0,len(self.a), 2))
        team2 = sum(self.a[i] for i in range(1,len(self.a), 2))
        return [team1,team2]

ls = [50,60,60,45,70]
alternating_sums = AltermatingSums(ls)
print(alternating_sums.alternating_sums())
