# If the marks obtained by a student in five different subjects are input through the keyboard,
# find out the aggregate marks and percentage marks obtained by the student. Assume that the
# maximum marks that can be obtained by a student in each subject is 100
total_marks = 500
marks_math = int(input('Enter marks in math:'))
marks_physics = int(input('Enter marks in physics:'))
marks_chem = int(input('Enter marks in chem:'))
marks_comp = int(input('Enter marks in comp:'))
marks_ecology = int(input('Enter marks in ecology:'))
obtain_marks = marks_chem + marks_comp + marks_ecology + marks_math + marks_physics
percentage_marks = (obtain_marks/500)*100
print('Total percentage obtain :', percentage_marks)
print('Total aggregate marks obtain :', obtain_marks)
