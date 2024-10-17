class Century:
    def __init__(self,year):
        self.year = year
    def get_century(self):
        return (self.year -1) // 100 + 1

year = int(input("Enter year: "))
century = Century(year)
print(century.get_century())