
import math
pi = math.pi
print ("pi is the value of {mypi}".format(mypi=pi))

import random
i = random.randint(0,100)
i

if (i < 50):
    print("i is less than 50")
elif (i > 50):
    print("1 is greater than 50")



picked_fruit = random.choice(['orange', 'strawberry', 'bananas'])

if picked_fruit == "orange":
    print("you're orange juilias")
elif picked_fruit == "strawberry":
    print("your're super strawberry")
else:
    print("you're are bananas")



def mycalc(num1, num2):
    result = (num1 * num2)
    return result


mycalc(12, 96)
mycalc(48, 17)

