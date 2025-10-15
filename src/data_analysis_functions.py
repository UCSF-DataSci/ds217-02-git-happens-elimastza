#! /usr/bin/python

def load_data(filepath):
    with open("data/students.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
    return lines
lines = load_data("data/students.csv")

with open('analysis_report.txt', 'a') as file:
 file.write("Analysis completed\n")

#Figure out min and max grades

def min_grade(grades):
    if not grades: 
       return 0 
    grades = [53, 67, 93, 80, 88, 95, 75, 90, 95, 100]
    return min(grades)


def max_grade(grades):
    if not grades: 
       return 0 
    grades = [53, 67, 93, 80, 88, 95, 75, 90, 95, 100]
    return max(grades)

grades = [53, 67, 93, 80, 88, 95, 75, 90, 95, 100]

##count students by subject
def analyze_data(students):
    return len(math_students)
math_students = [line for line in lines if "Math" in line] #copilot helped figure out code structure in bracket
print(f"{len(math_students)}")

def count_datascience_students(students):
    return len(datascience_students)
datascience_students = [(line for line in lines if "Data Science" in line)]
print(f"{len(datascience_students)}")

def count_psych_students(students):
    return len(psych_students)
psych_students = [(line for line in lines if "Psychology" in line)]
print(f"{len(psych_students)}")

def count_history_students(students):
    return len(history_students)
history_students = [line for line in lines if "History" in line]
print(f"{len(history_students)}")

def count_anatomy_students(students):
    return len(anatomy_students)
anatomy_students = [line for line in lines if "Anatomy" in line]
print(f"{len(anatomy_students)}")

#Define letter grade ranges
def letter_grade(grades):

    """ 
    grades = "A" elif score >= 90
    grades = "B" elif score >= 80
    grades = "C" elif score >= 70
    grades = "D" elif score >= 60
    grades = "F" else"""

    letter_grades = []

    for grade in grades:
        if grade >= 90:
            letter_grades.append("A")
        elif grade >= 80:
            letter_grades.append("B")
        elif grade >= 70:
            letter_grades.append("C")
        elif grade >= 60:
            letter_grades.append("D")
        else:
            letter_grades.append("F")  

    return letter_grades

    ##I was having trouble exporting my letter grades to the output file so Copilot helped me define grade_lines 
    grades = [53, 67, 93, 80, 88, 95, 75, 90, 95, 100]
    grade_lines = ""
    for score in grades:
        grade_lines += f"Score: {score}, Grade: {letter_grade(score)}\n"
    ##Copilot helped me till here

 # This is a tuple, not a string

def main():
    print(letter_grade(grades))
    print(min_grade(grades))
    print(max_grade(grades))
    print(analyze_data(math_students))
    print(count_datascience_students(datascience_students))
    print(count_psych_students(psych_students))
    print(count_history_students(history_students))
    print(count_anatomy_students(anatomy_students))
    return

def save_report(filepath, report):
    with open(filepath, 'w') as file:
        file.write(str(report))

def generate_report(letter_grade, min_grade, max_grade, math_students, datascience_students, psych_students, history_students, anatomy_students):
    report = (
        f"Letter Grades: {letter_grade}\n",
        f"Minimum Grade: {min_grade}\n",
        f"Maximum Grade: {max_grade}\n",
        f"Math Students: {math_students}\n",
        f"Data Science Students: {datascience_students}\n",
        f"Psychology Students: {psych_students}\n",
        f"History Students: {history_students}\n",
        f"Anatomy Students: {anatomy_students}\n",

    )
    return report


report = generate_report(letter_grade(grades), min_grade(grades), max_grade(grades), len(math_students), len(datascience_students), len(psych_students), len(history_students), len(anatomy_students))


save_report('output/analysis_report_functions.txt', report)


