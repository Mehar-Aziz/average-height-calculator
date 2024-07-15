# Heights Average Calculator

This Python script calculates the average height of students based on user input. The steps include taking input, converting it to integers, summing the heights, counting the number of students, and then calculating and rounding the average height.

## How to Use

1. **Input**: The script prompts the user to input a list of student heights separated by spaces.
2. **Processing**:
   - Converts the input list from strings to integers.
   - Calculates the total height of all students.
   - Counts the number of students.
   - Calculates the average height and rounds it to the nearest whole number.
3. **Output**: The script prints the list of student heights, the total height, the number of students, and the average height rounded to the nearest whole number.

## Code Explanation

```python
# Prompt the user to enter student heights separated by spaces
student_heights = input("Enter the list of student heights ").split()

# Convert each height from string to integer
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# Calculate the total height of all students
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

# Count the number of students
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

# Calculate the average height and round it
average_height = total_height / number_of_students
average_height_rounded = round(average_height, 0)
print(f"The Average of student heights is {average_height_rounded}")
