# name = kipngeno
#student
# name-kipngeno
# id-34567789
# school-africode
# phone-0789098765

class Student:
    def __init__(self, name, id=None, school=None, phone=None):
        self.name = name
        self.id = id
        self.school = school
        self.phone = phone
        
student1 = Student(name="Kipngeno", id="37243378", school="Africode", phone="0789087654")
print(f"the student is {student1.name} with id number {student1.id} studying at {student1.school} with phone number {student1.phone}")