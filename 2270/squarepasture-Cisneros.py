import sys
sys.stdin = open("square.in", "r")

#we can assign the input values to individual variables.
x_1, y_1, x_2, y_2 = map(int, input().split())
x_3, y_3, x_4, y_4 = map(int, input().split())

#we can find the lowest, highest, left, and right point between
#the two pastures using min and max. 
l = min(x_1, x_3)
r = max(x_2, x_4)
b = min(y_1, y_3)
t = max(y_2, y_4)

#using the values, we need the largest difference
#between the sides and the top and bottom.
squarelength = max(r - l, t - b)

#squarelength gives us the largest side length used for the lengths of the square.
#We can square this to get the minimum area.
out = open("square.out", "w")
out.write(str(squarelength * squarelength))
out.close()