numbers = [1, 2, 3, 5, 4, 6]

# numbers.reverse()

print(numbers)

print(list(reversed(numbers)))

print(list(reversed("hello")))  # return ['o', 'l', 'l', 'e', 'h']

print("hello"[::-1])  # return olleh

result = ""

print(result.join(list(reversed("hello"))))  # return olleh


for num in reversed(range(1, 10 + 1)):
    print(num)
