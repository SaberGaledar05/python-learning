# *args
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_numbers(1, 5, 4, 7, 8))

numbers = [1, 2, 3, 4, 5, 6]

print(sum_numbers(*numbers))


# **kwargs
def showFullInfo(**info):
    for key, value in info.items():
        print(f"{key} : {value}")


info = {
    "name": "saber",
    "family": "galedar",
    "age": 21,
    "email": "saber05galedar@gmail.com",
}

showFullInfo(**info)


def any(a, b, *args, default_parameters="default", **kwargs):
    return [a, b, args, default_parameters, kwargs]


print(any(1, "s", 6, 2, "j", name="saber"))
