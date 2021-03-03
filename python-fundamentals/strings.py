# Endline
print("print(\"Giraffe\\nAcademy\")" + " ↴ ")
print("Giraffe\nAcademy")

print("\n")

# Character Escaping
print("print(\"\"Giraffe\" Academy\")" + " ↴ ")
print("\"Giraffe\" Academy")

name = "Danh"
print(name)

print("\n")

# Concatenation
print(name + " is cool")

# Basic string method
print(name.lower())

# Checks if string are all uppercase
name = "DANH" #should return true
print(name.isupper())

# Checks if string are all uppercase
name = "Danh" #should return false
print(name.isupper())

# Character array
print(name[0]) #should output "D"

# Find the first index of chracter 'a'
# output: 1
print(name.index("a"))

# Replace function
print(name.replace("nh", "ng"))