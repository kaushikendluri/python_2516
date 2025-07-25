# Student Tuition Discount calculation

student_name = (input("enter student name: "))
student_grade = int(input("enter student grade level: "))
base_tuition_fee = int(input("enter the base tuition fee: "))
discount_percentage = 0
academic_topper_status = input("enter wheather the student is an academic topper or not (yes/no) : ")

if not (1 <= student_grade <= 12):
    print("grade is not valid between 1 to 12")
    

else:
    discount = 0

    if (9 <= student_grade <= 12 ) :
        if academic_topper_status == "yes":
            discount_percentage = 20
        else:
            discount_percentage = 10
            
    elif 6 <= student_grade <= 8:
        discount_percentage = 5
    else:
        discount_percentage = 0

# additional discounts

additional_discount = 0
if student_grade == 10:
    additional_discount = 3
elif student_grade == 12:
    additional_discount = 5

# total discount and calculations

total_discount = discount_percentage + additional_discount

discount_amount = base_tuition_fee* total_discount / 100
final_tuition_fee = base_tuition_fee - discount_amount

print(f"student name : {student_name }")
print(f"student grade : {student_grade }")
print(f"academic topper : {academic_topper_status }")
print(f"base tuition fee : {base_tuition_fee }")
print(f"total discount : {total_discount }")
print(f"discount amount saved : {discount_amount }")
print(f"final tuition fee : {final_tuition_fee }")




