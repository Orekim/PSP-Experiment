import random

def getAnswer(answernumber):
    if answernumber == 1:
        return "This is the best answer!,I'm a genius!"
    elif answernumber == 2:
        return "It is correct"
    elif answernumber == 3:
        return "This is correct too"
    elif answernumber == 4:
        return "Yes"
    elif answernumber == 5:
        return "This is incorrect"
    elif answernumber == 6:
        return "Wrong!"
    elif answernumber == 7:
        return "Try again"
    elif answernumber == 8:
        return "NO!,I guess I'm not a smart computer"

r = random.randint(1,8)
Answer = getAnswer(r)
print(Answer)
