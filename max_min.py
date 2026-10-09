# Max
numbers = [5, 7, 90, 30, 105, 65]
characters = ["a", "h", "z", "t"]
myName = "saber"


print(max(numbers))  # 105
print(max(characters))  # z
print(max(myName))  # s


# Min

print(min(numbers))  # 5
print(min(characters))  # a
print(min(myName))  # a


# for exaple

names = ["saber", "mohammad", "akbar", "milad", "ali"]

result = [len(name) for name in names]

print(result)  # [5, 8, 5, 5, 3]

print(max(names, key=lambda name: len(name)))  # mohammad
print(min(names, key=lambda name: len(name)))  # ali
