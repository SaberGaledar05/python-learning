# parameters & arguments


def sum(num1, num2):
    return num1 + num2


print(sum(5, 9))

name = "Saber"
family = "Galedar"


def full_name(first_name, last_name):
    return f"{first_name} {last_name}"


print(full_name(name, family))
firstName = input("what is your name ")
lastName = input("what is your family ")

print(f"Hi {full_name(firstName, lastName)}")


# for exaple

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sum_odd_numbers(listOfNumber):
    total = 0
    for num in listOfNumber:
        if num % 2 != 0:
            total += num
    return total


print(sum_odd_numbers(myList))


# for exaple


def is_even_numbers(number):
    if number % 2 == 0:
        return True
    return False


print(is_even_numbers(15))
print(is_even_numbers(22))
