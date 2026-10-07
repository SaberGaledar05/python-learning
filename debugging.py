# import pdb

# pdb.set_trace()

number1 = int(input("please enter a number: "))
number2 = int(input("please enter a number: "))
result = number1 + number2

print(f"{number1} + {number2} = {result}")


# common pdb commands =
# n -> next line
# l -> your commands list
# c -> continue -> finished debugging


def add_numbers(a, b, c, d):
    import pdb

    pdb.set_trace()
    return a + b + c + d


res = add_numbers(1, 2, 3, 4)
print(res)
