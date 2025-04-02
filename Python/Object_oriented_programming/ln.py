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




class User:
    def __init__(self, name, phone, is_admin=False, is_logged_in=False):
        self.name= name
        self.phone = phone
        self.is_admin = is_admin
        self.is_logged_in = is_logged_in
    def user_login(self):
        if self.is_admin and self.is_logged_in:
            return "Dashboard"
        elif not self.is_logged_in:
            return "Login page"
        else:
            return "Newsfeed"
        
# user1 = User(name="Kipngeno", phone="0789098756", is_admin=True, is_logged_in=True)
# print(f"the name is {user1.name} with phone number {user1.phone} and should be taken to {user1.user_login()}")
# user2 = User(name="Kirui", phone="0787656789", is_logged_in=False)    
# print(f"the name is {user2.name} with phone number {user2.phone} and is directed to {user2.user_login()}")
user3 = User(name="ngepet", phone="0787656789", is_admin=False, is_logged_in=True)    
print(f"the name is {user3.name} with phone number {user3.phone} and is directed to {user3.user_login()}")