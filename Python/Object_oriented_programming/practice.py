#student
# name-kipngeno
# id-34567789
# school-africode
# phone-0789098765

class Student:
    def __init__(self, name, id, school, phone):
        self.name = name
        self.id = id
        self.school = school
        self.phone = phone
        
# student1 = Student(name="Kipngeno", id="37243302", school="Africode", phone="0719890987")
# print(f"the student name is {student1.name} with id number {student1.id} studying at {student1.school} with phone number {student1.phone}")
# student2 = Student(name="Rop", id="376789098", school="Africode", phone="0789678098")
# print(f"the student name is {student2.name} with id number {student2.id} studying at {student2.school} with phone number {student2.phone}")
student3 = Student(name="Dorothy", id="375645433", school="Africode", phone="0745777163")
print(f"the student name is {student3.name} with id number {student3.id} studying in {student3.school} with phone number {student3.phone}")