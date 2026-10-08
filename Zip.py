# zip

number_1 = [1, 2, 3, 4, 5]
number_2 = [5, 6, 7, 8, 9, 10]

result = zip(number_1, number_2)

# print(list(result)) # [(1, 5), (2, 6), (3, 7), (4, 8), (5,9)]
print(dict(result))  # {1: 5, 2: 6, 3: 7, 4: 8, 5: 9}

mylist = [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9)]

print(list(zip(*mylist)))


students = ["mahammad", "iman", "saber"]
midTerm = [80, 58, 90]
finalTerm = [69, 95, 87]

final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midTerm, finalTerm)}

print(final_grades)

final_grades2 = zip(students, map(lambda t: max(t), zip(midTerm, finalTerm)))
#final_grades2 = zip(students, map(lambda t: (t[0] + t[1]) / 2, zip(midTerm, finalTerm))) ## for average
print(dict(final_grades2))
