num_students = int(input("Enter the total number of students: "))

i = 1
while i <= num_students:
    total_grade = 0
    num_subject = int(input(f"Enter the number of subjects for student {i}: "))
    
    for j in range(1, num_subject + 1):
        grade = float(input(f"Enther the subject {j} grade for student {i}: "))
        total_grade += grade
        
        average_grade = total_grade / num_subject
        print (f"average grade for student{i}: {average_grade:.2f}")
        i += 1