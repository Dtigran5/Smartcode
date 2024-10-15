import random

class HarryPotter():
    def __init__(self,attempts):
        self.attempts = attempts
        self.voldemort_words = ['Avada Kedavra', 'Crucio', 'Imperio']
        random.shuffle(self.voldemort_words)
    
    def fight(self):
        score = 0
        for i in range(3):
            if self.attempts[i] == self.voldemort_words[i]:
                score += 1
            else:
                score -=1
        if score >= 2:
            return self.voldemort_words, "You win"
        else:
            return self.voldemort_words, "You lose"

attempts = ['Avada Kedavra', 'Crucio', 'Imperio']
fight_test = HarryPotter(attempts)
print(fight_test.fight())
