student_heights = input("Enter the list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height = total_height / number_of_students
average_height_rounded = round(average_height, 0)
print(f"The Average of student heights is {average_height_rounded}")