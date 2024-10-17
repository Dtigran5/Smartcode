class LuckyTicket:
    def __init__(self,n):
        self.n = str(n)
    def is_lucky(self):
        half_len = len(self.n) // 2
        first_half = sum(map(int, self.n[:half_len]))
        second_half = sum(map(int, self.n[half_len:]))
        return first_half == second_half

n = int(input("Enter number: "))
lucky_ticket = LuckyTicket(n)
print(lucky_ticket.is_lucky())