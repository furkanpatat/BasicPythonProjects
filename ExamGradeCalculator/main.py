"""
Calculate the letter grade according to the user's exam1, exam2, final grades
 and grades entered by the user.

     exam1 will affect 30% of the total grade.

     exam2 will affect 30% of the total grade.

     The final will count for 40% of the total grade.
"""
exam1 = int(input("Exam1: "))
exam2 = int(input("Exam2: "))
final = int(input("Final: "))

exams_result = (exam1 * (30/100)) + (exam2 * (30/100)) + (final * (40/100))

if(exams_result >= 90):
    print(exams_result," -> AA")
elif(exams_result >= 85):
    print(exams_result," -> BA")
elif(exams_result >= 80):
    print(exams_result," -> BB")
elif(exams_result >= 75):
    print(exams_result," -> CB")
elif(exams_result >= 70):
    print(exams_result,"-> CC")
elif(exams_result >= 65):
    print(exams_result," -> DC")
elif(exams_result >= 60):
    print(exams_result," -> DD")
elif(exams_result >= 55):
    print(exams_result," -> FD")
elif(exams_result < 55):
    print(exams_result," -> FF")
else:
    print("Incorrect Entry")