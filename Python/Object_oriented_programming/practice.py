#student
# name-kipngeno
# id-34567789
# school-africode
# phone-0789098765

# class Student:
#     def __init__(self, name, id, school, phone):
#         self.name = name
#         self.id = id
#         self.school = school
#         self.phone = phone
        
# student1 = Student(name="Kipngeno", id="37243302", school="Africode", phone="0719890987")
# print(f"the student name is {student1.name} with id number {student1.id} studying at {student1.school} with phone number {student1.phone}")
# student2 = Student(name="Rop", id="376789098", school="Africode", phone="0789678098")
# print(f"the student name is {student2.name} with id number {student2.id} studying at {student2.school} with phone number {student2.phone}")
# student3 = Student(name="Dorothy", id="375645433", school="Africode", phone="0745777163")
# print(f"the student name is {student3.name} with id number {student3.id} studying in {student3.school} with phone number {student3.phone}")





# class Student:
#     def __init__(self, name, school, course, marital_status):
#         self.name = name
#         self.school = school
#         self.course = course
#         self.marital_status = marital_status
        
    
    
    
    
# student3 = Student(name="Abnas", school="Africode", course="IT", marital_status="single")
# print(f"{student3.name}  studying {student3.course} at {student3.school} is {student3.marital_status}")

# class Employee:
#     def __init__(self, name, company, in_list=False, in_black_list=False):
#         self.name = name
#         self.company = company
#         self.in_list = in_list
#         self.in_black_list = in_black_list
        
    
#     def employee_status(self):
#         if self.in_list and self.in_black_list:
#             return "Employed"
#         elif not self.in_list:
#             return "Visitor"
#         else:
#             return "intruder"    
        
# employee1 = Employee(name="Jare", company="Watu credit", in_list=True, in_black_list=True)
# print(f"{employee1.name} working for {employee1.company} is {employee1.employee_status()}")
# employee2 = Employee(name="Onesmus", company="Hiline", in_list=False, in_black_list=True)
# print(f"{employee2.name} working for {employee2.company} is {employee2.employee_status()}")
# employee3 = Employee(name="Natasha", company="M-kopa", in_list=True, in_black_list=False)
# print(f"{employee3.name} working for {employee3.company} is an {employee3.employee_status()}")

class User:
    def __init__(self, name, is_admin=False, is_logged_in=False):
        self.name = name
        self.is_admin = is_admin
        self.is_logged_in = is_logged_in
        
    def user_status(self):
        if self.is_admin and self.is_logged_in:
            return "Dashboard"
        elif not self.is_logged_in:
            return "Login page"
        else:
            return "Newsfeed"

user1 = User(name="Alfred", is_admin=True, is_logged_in=True)
print(f"{user1.name} is directed to the {user1.user_status()}")
user2 = User(name="Kinuthia", is_admin=True, is_logged_in=False)
print(f"{user2.name} is directed to the {user2.user_status()}")
user3 = User(name="Kimani", is_admin=False, is_logged_in=True)
print(f"{user3.name} is directed to the {user3.user_status()}")
        
    




