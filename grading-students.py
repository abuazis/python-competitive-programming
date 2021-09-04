# Grading Students Challenge
# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents():
    # Catch input score value
    grades_count = int(input().strip())

    # Initial grades variable
    grades = []

    # Loop for appending input score into grades variable
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    # Looping to check and run grading logic
    for i in grades:
        if i >= 38:
            if i % 5 == 3:
                i += 2
            elif i % 5 == 4:
                i += 1
        print(i)

if __name__ == '__main__':
    # Run logic function
    gradingStudents()