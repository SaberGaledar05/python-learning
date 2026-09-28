# map

numbers = [1, 2, 3, 4, 5]

doubles = map(lambda num: num**2, numbers)

print(doubles)

print(list(doubles))


names = ["Saber", "arash"]

upper = map(lambda x: x.upper(), names)


print(list(upper))

people = [
    {"name": "saber", "family": "galedar", "age": 21},
    {"name": "arash", "family": "galedar", "age": 31},
]
families = map(lambda person: person["family"], people)

print(list(families))
# or
families_2 = []
for person in people:
    families_2.append(person["family"])
print(families_2)
