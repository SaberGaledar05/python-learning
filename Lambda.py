# Lambda


def square(num):
    return num * num


print(square(6))

myFunction = lambda num: num * num

print(myFunction(6))


def sum(num1, num2):
    return num1 + num2


sum2 = lambda num1, num2: num1 + num2

print(sum(4, 9))
print(sum2(4, 9))


print(square.__name__)  # print name of function
