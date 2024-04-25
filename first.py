import math
n = int(input("number of stairs:")) + 1
a = int((((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n)/math.sqrt(5))
print("number of ways to climb that stair - ",a)