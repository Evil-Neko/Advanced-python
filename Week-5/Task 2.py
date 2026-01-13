import json

with open("students.json", "r") as file:
    students = json.load(file)

for i in students:
    grades = i["grades"]
    i["average_grade"] = sum(grades)/len(grades)

with open("updated_students.json", "w") as file:
    json.dump(students, file, indent=4)