# Function definition
def sayHi(name):
    print("Hi, " + name + ".")

def calculateCube(number):
    return number * number * number

name = input("Enter name: ")
sayHi(name)
number = float(input("Enter number to cube: "))
numberCubed = calculateCube(number)
print(str(number) + " cubed is " + str(numberCubed))