# filter

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

evens = filter(lambda num: num % 2 == 0, numbers)

print(list(evens))

users = [
    {"name": "ali", "shopCart": []},
    {"name": "mohammad", "shopCart": [1, 2, 3, 4]},
    {"name": "reza", "shopCart": []},
]

print(len(users))

result = filter(lambda user: len(user["shopCart"]) == 0, users)
# OR
# result = filter(lambda user: not user["shopCart"], users)

print(list(result))

result2 = map(
    lambda user: user["name"], filter(lambda user: len(user["shopCart"]) == 0, users)
)

print(list(result2))

result3 = [user["name"] for user in users if len(user["shopCart"]) == 0]

print(result3)

# all

my_numbers = [2, 4, 6, 8]

print(all([num % 2 == 0 for num in my_numbers]))

# any

my_number2 = [2, 4, 6, 7]

print(any([num % 2 != 0 for num in my_number2]))
