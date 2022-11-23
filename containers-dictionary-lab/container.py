# Exercise1
# students = ['Sabika','Layla', 'Ranya', 'Sharifa', 'Hessa', 'Fatima', 'Kareem', 'Alex']
# print(students[1])
# print(students[-1])


#Exercise2
foods = ('pizza', 'pasta', 'sushi', 'Koshary', 'Steak')
# for food in foods:
#     print(f"{food} is a good food")


# Exercise3
# for food in foods[1:3]:
#               or [-2:]:
#     print(f"{food} is a good food")


# Exercise4
# home_town = {
#     'city': 'Manama',
#     'state': 'Bahrain',
#     'population': '600,000'
# }
# print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")


# Exercise5
# for key, value in home_town.items():
#     print(f"{key} = {value}")


# Exercise6
# cohort = []
# student = [
#     {
#         'student': 'Sabika',
#         'fav_food': 'Chocolate',
#     },
#     {
#         'student': 'A.Rahman',
#         'fav_food': 'Sea Food',
#     },

#     {
#         'student': 'Fatima',
#         'fav_food': 'French Fries',
#     },
# ]

# for s in students:
#     cohort.append(s)
#     print(cohort)
# for idx, name in enumerate(students):
#     cohort.append({
#         'name': name,
#         'fav_food': foods[idx]
#         })

# for student in cohort:
#     print(student


# Exercise7
# awesome_students = []
# for idx, name in enumerate(students):
#     awesome_students.append({
#         'name': name
#         })

# for student in awesome_students:
#     print(f"{student['name']} is awesome!")


# Exercise8
# for food in foods:
#     if 'a' in food:
#         print(food)