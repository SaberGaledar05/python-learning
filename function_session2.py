def square_of_7():
    print(7**2)


square_of_7()


def square_of_8():
    print("i am before return")
    return 8**2
    print("i am after return")


result = square_of_8()

print(square_of_8())
print(result)
# these are equal because it return a value


# for example
def add_number():
    a = 5
    b = 6
    return a + b


print(add_number())  # return 11


