#! /usr/bin/python
with open("data/students.csv", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
#Copilot helped figure out code structure along with lecture slides
def calculate_average(grades):
    if not grades: 
       return 0 
    return sum(grades)/len(grades)
grades = [53, 67, 93, 80, 88, 95, 75, 90, 95, 100]
avg = calculate_average(grades)
print(f"Average grade: {avg:.1f}")

#count total students
def total_students(students):
    return len(total_students)
total_students = ["Amy", "Paul", "Pia", "Mark", "Johnny", "Peter", "Jenny", "Theo", "Lucy", "Elizabeth"]
print(f"{len(total_students)}")

##count students by subject
def count_math_students(students):
    return len(math_students)
math_students = [line for line in lines if "Math" in line] #copilot helped figure out code structure in bracket
print(f"{len(math_students)}")

def count_datascience_students(students):
    return len(datascience_students)
datascience_students = [line for line in lines if "Data Science" in line]
print(f"{len(datascience_students)}")

def count_psych_students(students):
    return len(psych_students)
psych_students = [line for line in lines if "Psychology" in line]
print(f"{len(psych_students)}")

def count_history_students(students):
    return len(history_students)
history_students = [line for line in lines if "History" in line]
print(f"{len(history_students)}")

def count_anatomy_students(students):
    return len(anatomy_students)
anatomy_students = [line for line in lines if "Anatomy" in line]
print(f"{len(anatomy_students)}")


#Copilot helped figure out code structure (used explain function to help understand what the problem was)
def save_report(filepath, content):
    with open(filepath, "w") as file:
        file.write(str(content))

def generate_report(total_students, avg_grade, math_students, datascience_students, psych_students, history_students, anatomy_students, count_subjects):
    report = (
        f"Total # of Students: {total_students}\n",
        f"Average Grade: {avg_grade: .1f}\n",
        f"Math Students: {math_students}\n",
        f"Data Science Students: {datascience_students}\n",
        f"Psychology Students: {psych_students}\n",
        f"History Students: {history_students}\n",
        f"Anatomy Students: {anatomy_students}\n",

    )
    return report

def count_subjects(subjects):
    return len({len(math_students), len(datascience_students), len(anatomy_students), len(history_students), len(psych_students)})

count_subjects == {len(math_students), len(datascience_students), len(anatomy_students), len(history_students), len(psych_students)}

report = generate_report(len(total_students), avg, len(math_students), len(datascience_students), len(psych_students), len(history_students), len(anatomy_students), count_subjects)

save_report('output/analysis_report.txt', report)


def main():
    print(calculate_average(grades))
    print(total_students)
    print(count_math_students(math_students))
    print(count_datascience_students(datascience_students))
    print(count_psych_students(psych_students))
    print(count_history_students(history_students))
    print(count_anatomy_students(anatomy_students))
    print(count_subjects(count_subjects))


if __name__ == "__main__":
    main()
save_report('output/analysis_report.txt', report)