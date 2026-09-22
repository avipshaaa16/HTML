students = {
    "Avipsha": 90,
    "Prisha": 94,
    "Arpita":84,
    "Saujanya":88,
    "Aaryashree":97
}

average = sum(students.values())/len(students)
print("Class average:",average)
highest_student = max(students, key = students.get)
lowest_student = min(students, key = students.get)

print("Hightest scorer:", highest_student, students[highest_student])
print("Lowest scorer:", lowest_student , students[lowest_student])

name = input("Enter a student's name:")
mark = students.get(name,"Student not found")

print("mark:", mark)