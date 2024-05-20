# Create a program that allows for managing a student database.
# The program should have the following functionalities:
# 1. Add a new student(first name, last name, age, grades)
# 2. Display a list of all students in a user-friendly format
# 3. Display average grade for each student
# 4. Remove a student based on their last name
# 5. Use list comprehension to create a list containing only students who have a grade greater than 4
# Use only functional programming

students = [["Joe", "Biden", 20, [2, 3, 3, 2]], ["Donald", "Trump", 21, [3, 4, 5, 5]],
            ["Barack", "Obama", 19, [4, 5, 5, 5]], ["George", "Bush", 17, [2, 3, 4, 5]]]

print(f"Welcome to student database!")
choice = 0
while choice != 6:
    print(f"1. Add new student")
    print(f"2. Display all students")
    print(f"3. Display average grade for each student")
    print(f"4. Remove student")
    print(f"5. List students that has grade greater or equal to 4")
    print(f"6. Exit")
    choice = int(input(f"Enter your choice: "))
    if choice == 1:
        fName = input(f"Enter first name: ")
        lName = input(f"Enter last name: ")
        age = int(input(f"Enter age: "))
        grades = []
        grade = 1
        while grade != 0:
            grade = int(input(f"Enter grade (0 to exit): "))
            if grade != 0:
                grades.append(grade)
        students.append([fName, lName, age, grades])
        print(f"Student added!")

    if choice == 2:
        for student in students:
            print(f"First name: {student[0]}, Last name: {student[1]}, "
                  f"Age: {student[2]}, Grades: {student[3]}")
    if choice == 3:
        for student in students:
            averageGrade = sum(student[3]) / len(student[3])
            print(f"Last name: {student[1]}, Average grade: {averageGrade}")

    if choice == 4:
        std = input(f"Enter last name of student that you want to remove: ")
        for student in students:
            if student[1] == std:
                students.remove(student)
                print(f"Student removed!")

    if choice == 5:
        for student in students:
            for grade in student[3]:
                if grade >= 4:
                    print(f"Last name: {student[1]}, Grades: {student[3]}")
                    break;

    if choice == 6:
        print(f"Goodbye!")


