import csv
import os

print("====================================")
print("   STUDENT PERFORMANCE ANALYZER")
print("====================================")

student_name = input("Enter student's name: ")
print(f"Welcome, {student_name}! ")

while True:
    try:
        number_of_subjects = int(input("How many subjects do you want to enter? "))

        if number_of_subjects > 0:
            break
        else:
            print("Please enter at least 1 subject.")

    except ValueError:
        print("Invalid number! Please enter a whole number.")

print(f"You have entered {number_of_subjects} subjects.")

subjects = []

for i in range(number_of_subjects):
    while True:
     subject_name = input("Enter subject name: ").strip()

     if subject_name:
        break
     else:
        print("Subject name cannot be empty.")

    while True:
        try:
            maximum_marks = int(input("Enter maximum marks: "))

            if maximum_marks > 0:
                break
            else:
                print("Maximum marks should be greater than 0.")

        except ValueError:
            print("Invalid number! Please enter a whole number.")

    while True:
        try:
            marks_obtained = int(input("Enter marks obtained: "))

            if 0 <= marks_obtained <= maximum_marks:
                break
            else:
                print(f"Please enter marks between 0 and {maximum_marks}.")

        except ValueError:
            print("Invalid number! Please enter a whole number.")

    subjects.append({
        "name": subject_name,
        "maximum_marks": maximum_marks,
        "marks_obtained": marks_obtained
    })

print("\nSubjects entered:")

for subject in subjects:
    print(
        subject["name"],
        "- Maximum:", subject["maximum_marks"],
        ", Obtained: ", subject["marks_obtained"]
    )    

total_obtained = 0
total_maximum = 0

for subject in subjects:
    total_obtained += subject["marks_obtained"]
    total_maximum += subject["maximum_marks"]

print("\nTotal marks obtained:", total_obtained)
print("Total maximum marks:", total_maximum)

percentage = (total_obtained / total_maximum) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 90:
    print("Performance: Excellent!")
elif percentage >= 80:
    print("Performance: Very Good!")
elif percentage >= 70:
    print("Performance: Good!")
elif percentage >= 60:
    print("Performance: Satisfactory.")
else:
    print("Performance: Needs Improvement.")

highest_subject = max(subjects, key=lambda subject: subject["marks_obtained"] / subject["maximum_marks"])
lowest_subject = min(subjects, key=lambda subject: subject["marks_obtained"] / subject["maximum_marks"])

highest_percentage = (highest_subject["marks_obtained"] / highest_subject["maximum_marks"]) * 100
lowest_percentage = (lowest_subject["marks_obtained"] / lowest_subject["maximum_marks"]) * 100

print("\nBest-performing subject:", highest_subject["name"])
print(f"Subject percentage: {highest_percentage:.2f}%")

print("\nLowest-performing subject:", lowest_subject["name"])
print(f"Subject percentage: {lowest_percentage:.2f}%")

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , "student_results.csv")

with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Student Name",
        "Subject",
        "Maximum Marks",
        "Marks Obtained",
        "Percentage"
    ])

    for subject in subjects:
        subject_percentage = (
            subject["marks_obtained"] / subject["maximum_marks"]
        ) * 100

        writer.writerow([
            student_name,
            subject["name"],
            subject["maximum_marks"],
            subject["marks_obtained"],
            f"{subject_percentage:.2f}"
        ])

print("\nResults saved to student_results.csv")

