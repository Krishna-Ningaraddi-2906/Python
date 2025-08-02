# Comparision

import math as math
import random as random

print(1 < 2)
print("1==2", 1 == 2)
print(1 < 2)
print(1 < 2)

print(1 < 2 == 3)  # which is equal to 1<2 and 2==3

print(1 == 2 < 3)  # which is equal to 1==2 and 2<3

print(math.floor(5/2))
print(math.ceil(5/2))

print(math.floor(-3.5/2))

print(math.trunc(2.8))  # this take the value towards the 0 value
print(math.trunc(-2.8))

print((2+3j)*3)

nums = [1, 5, 6, 8, 9, 7, 10, 2, 5]
print(random.choice(nums))
random.shuffle(nums)
print(nums)

setOne = {1, 2, 3}
setTwo = {1, 5, 9}

print("intersection", setOne & setTwo)
print("Union", setOne | setTwo)
