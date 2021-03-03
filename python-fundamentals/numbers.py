arg1 = 3
arg2 = 4.5
print(str(arg1) + " + " + str(arg2) + " = " + str(arg1 + arg2))

# Order of operation
arg1= 3
arg2 = 4
arg3 = 5
print(str(arg1) + " * " + str(arg2) + " + " + str(arg3) + " = " + str(arg1 * arg2 + arg3))
# Result: 17
print(str(arg1) + " * " + "(" + str(arg2) + " + " + str(arg3) + ") = " + str(arg1 * (arg2 + arg3)))
# Result: 27

# Modulus gives us remainder
arg1 = 10
arg2 = 3
print(str(arg1) + " % " + str(arg2) + " = " + str(arg1 % arg2))
# Remainder: 1

# Convert numbers as a string
number = 2
print(str(number))

# Power
# 3 squared = 9
arg1 = 3
arg2 = 2
print(str(arg1) + " raised to the power of " + str(arg2) + " is " + str(pow(arg1, arg2)))

arg1 = 1
arg2 = 5
# Max returns the larger of the two number
print("max(" + str(arg1) + ", " + str(arg2) + ") = " + str(max(arg1, arg2)))
# Min returns the smaller of the two number
print("min(" + str(arg1) + ", " + str(arg2) + ") = " + str(min(arg1, arg2)))

# Rounding
# Result: 2
numberToRound = 1.8
print(str(numberToRound) + " rounded is..." + str(round(numberToRound)))
