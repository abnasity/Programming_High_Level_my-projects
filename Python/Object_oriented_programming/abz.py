class Employee:
    def __init__(self, name, company, in_list=False, in_blacklist=False):
        self.name = name
        self.company = company
        self.in_list = in_list
        self.in_blacklist = in_blacklist
        
    def employee_status(self):
        if self.in_list:
            return "Employed"
        elif self.in_blacklist:
            return "Visitor"
        else:
            return "intruder"
        
# employee1 = Employee(name="Calvin", company="Diamond tree", in_list=True, in_blacklist=True)
# print(f"{employee1.name} walking for {employee1.company} is {employee1.employee_status()}")

# employee2 = Employee(name="Jare", company="Hiline", in_list=False, in_blacklist=True)
# print(f"{employee2.name} walking for {employee2.company} is {employee2.employee_status()}")


class User:
    def __init__(self, name, is_logged_in=False, is_admin=False):
        self.name = name
        self.is_logged_in = is_logged_in
        self.is_admin = is_admin
        
    def user_status(self) -> str:
        if  self.is_admin and self.is_logged_in:
            return "Dashboard"
        elif not self.is_admin:
            return "Login page"
        else:
            return "Newsfeed"
        
user1 = User(name="abnas", is_admin=True, is_logged_in=True)
print(f"{user1.name} is directed to {user1.user_status()}")

user2 = User(name="collo", is_admin=False, is_logged_in=False)
print(f"{user2.name} is directed to {user2.user_status()}")

user3 = User(name="2pac", is_admin=False, is_logged_in=False)
print(f"{user3.name} is directed to {user3.user_status()}")