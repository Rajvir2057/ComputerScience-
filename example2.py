def main() :
    result = cubeVolume(2)
    print("A cube with side length 2 has volume", result)

def cubeVolume(sideLength) :
    volume = sideLength ** 3
    return volume

main()

def totalCents(dollars, cents) :
    result = dollars * 100 + cents
    return result
print(totalCents(30,12))

def boxString(contents) :
    n = len(contents)
    if n == 0 :
        return # Return immediately
    print("-" * (n + 2))
    print("!" + contents + "!")
    print("-" * (n + 2))

boxString("Hello World")

def main() :
    sum = 0
    for i in range(11) :
        square = i * i
        sum = sum + square
    print(square, sum)

main()

def main():
    for i in range(1, 11):  # Loops from 1 to 10 (inclusive)
        square = i * i  # Computes square of i
        print(square, end=" ")  # Print each square on the same line

main()
print("\n")

a = "college"
e = list(a)
print(e)

b = []
c = b.append(1)
d= b.insert(0,12)
print(b)

fruits= ["apples","bananas","orange"]
adding = fruits.insert(3,"berries")
print(fruits)
popping = fruits.reverse()
print(fruits)

values = [1,2,3,4,5]
def multiply(values,factor):
    for i in range(len(values)):
        values[i] = values[i] * factor
    return values
result1 = multiply(values,10)
print(result1)

def printTriangle(sideLength) :
    if sideLength < 1 : return
    printTriangle(sideLength - 1)
    print("\t*" * sideLength)
printTriangle(9)

