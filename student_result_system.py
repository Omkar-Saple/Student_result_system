students = [
    {"id": 101, "name": "Amit", "marks": 85},
    {"id": 102, "name": "Priya", "marks": 92},
    {"id": 103, "name": "Rahul", "marks": 67},
    {"id": 104, "name": "Sneha", "marks": 78},
    {"id": 105, "name": "Vikram", "marks": 55},
    {"id": 106, "name": "Neha", "marks": 88},
    {"id": 107, "name": "Arjun", "marks": 73},
    {"id": 108, "name": "Pooja", "marks": 95},
    {"id": 109, "name": "Rohan", "marks": 61},
    {"id": 110, "name": "Kavya", "marks": 81}
]


def student_result(students):
    for student in students:
        print(student["name"], "-", student["marks"])


def highest_mark(students):
    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    return highest["name"]


def lowest_mark(students):
    lowest = students[0]

    for student in students:
        if student["marks"] < lowest["marks"]:
            lowest = student

    return lowest["name"]


def student_average(students):
    total = 0

    for student in students:
        total += student["marks"]

    return total / len(students)


def greater_80(students):
    result = []

    for student in students:
        if student["marks"] > 80:
            result.append(student["name"])

    return result


def lesser_40(students):
    result = []

    for student in students:
        if student["marks"] < 40:
            result.append(student["name"])

    return result


student_result(students)

print("\nTopper:", highest_mark(students))
print("Lowest:", lowest_mark(students))
print("Average:", student_average(students))
print("Greater than 80:", greater_80(students))
print("Less than 40:", lesser_40(students))
