number1 = [1,2,3,4,5]
number2 = [2,4,6,8,10]
result = list(map(lambda x,y: x+y ,number1,number2))
print(result)

num= [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq,num))
print(square)