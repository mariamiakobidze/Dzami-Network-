# for i in range (5, 20, 2): # 1 da 2 dor ragne and 3 for step 
#     print(i)
    
    
# name = input ("input your name:")

# def helou (saxeli):
#     print('HELLO ' + saxeli)
    
# helou(name)


# def max(x, y): 
#     return x + y
    
# z= max(5,10)
# print(z)




# def multiply(a, b):
#     return a * b


def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum