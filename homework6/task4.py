#link -> https://www.codewars.com/kata/604287495a72ae00131685c7
def doubleton(num):
    num += 1
    while len(set(str(num))) != 2:
        num+= 1
    return num

print(doubleton(120))   
print(doubleton(1234)) 
print(doubleton(10))    
