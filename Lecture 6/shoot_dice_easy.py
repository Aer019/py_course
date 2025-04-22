import random 

user_result = int(input('Put 1 2 or 3 to play the dice -->'))
comp_result = random.randint(1,4)

win_or_not = 'you win' if user_result == comp_result \
                else 'you lose'
print(win_or_not)
