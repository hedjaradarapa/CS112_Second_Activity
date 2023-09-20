student_name= input("Student name:")
ID= input("ID:")
course_section = input("Course and Section:")
first_quarter_grade = eval(input("First Quarter Grade:"))
second_quarter_grade = eval(input("Second Quarter Grade:"))
third_quarter_grade = eval(input("Third Quarter Grade:"))
fourth_quarter_grade = eval(input("Fourth Quarter Grade:"))

ave = (first_quarter_grade + second_quarter_grade + third_quarter_grade + fourth_quarter_grade) / 4

print("student_name", student_name)
print("ID", ID)
print("course section", course_section)
print("first quarter_grade", first_quarter_grade)
print("second quarter_grade", second_quarter_grade)
print("third quarter grade", third_quarter_grade)
print("fourth quarter grade", fourth_quarter_grade)
print("final average:", ave)