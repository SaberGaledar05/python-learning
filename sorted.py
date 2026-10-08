# sort
numbers = [56, 34, 89, 24, 16, 6, 1]

numbers.sort()

print(numbers)

result = sorted(numbers)

print(result)


users = [
    {"name": "saber", "family": "galedar", "age": 21},
    {"name": "ali", "family": "alvandi", "age": 22},
    {"name": "mohammad", "family": "ahmadi", "age": 25},
]

print(sorted(users, key=lambda user: user["name"], reverse=True))
