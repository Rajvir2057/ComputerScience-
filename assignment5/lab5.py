#Kaur Rajvir 816815

x = 10   
def calculation(a,b,c, d=2):
    """
    This function returns the value of (a*b+c*d)
    """
    result = a*b+c*d
    return result

result1 = calculation(5,4,3) 
print(result1)                 
result2 = calculation(5,4,3,1)
print(result2)
result3 = calculation(5,4,3,x)
print(result3)