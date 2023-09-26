import random

num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))

num_list = list(range(num1, num2))

random_numbers = [random.choice(num_list) for i in range(3)]
print(random_numbers)