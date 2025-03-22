a = 100000
b= a//1000
print(b)

def addition(num1,num2):
    sum = num1 + num2
    return sum

print("the sum is" ,addition(10, 20))

def cubeVolume(sideLength) :
    volume = sideLength ** 3
    return volume

result1 = cubeVolume(2)
result2 = cubeVolume(10)

print("A cube with side length 2 has volume", result1)
print("A cube with side length 10 has volume", result2)


def result(n):
    list1 = []
    for i in range(n):
        list1.append(i*i)
    return list1
answer1 = result(2)
answer3= result(10)
print(answer1)
print(answer3)

def squares(g):
    if g <= 0:
        return []
    else:
        return squares(g - 1) + [g * g]

print(squares(5))

def squares2(c):
    if c <= 0:
        return 0
    else:
        return squares2(c - 1) + c*c
    
print(squares2(5))

list1 = [1,3,2,4,5,6]
list2 = list1 *2
print(list2)

list3 = list1 + list2
print(list3)

names =[2000,1945,1789,1894]
names.sort()
print(names)

