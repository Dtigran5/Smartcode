import math

class Covid19Detection:
    def __init__(self, temperature_celsius):
        self.temperature = temperature_celsius
    
    def check_coronavirus(self):
        result = math.ceil(self.temperature * math.pi)
        if 120 <= result <= 128:
            return "You have coronavirus"
        else:
            return "Everything is ok"
temperature = float(input("Enter your temperature: "))
covid_test = Covid19Detection(temperature)
print(covid_test.check_coronavirus()) 
       