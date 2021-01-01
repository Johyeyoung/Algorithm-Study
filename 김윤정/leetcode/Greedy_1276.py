# [Greedy] 1276. Number of Burgers with No Waste of Ingredients

# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

# 4x + 2y = 16
# x + y =7



tomato=16 
cheese =7

jumbo = int((tomato -2 * cheese)/2)
print(jumbo)
small = cheese - jumbo

if jumbo >= 0 and small >=0:
    print([jumbo, small])
else :
    print([])

