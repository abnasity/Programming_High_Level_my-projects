
class Employee:
    def __init__(self, name, company, pay, in_list=False, in_blacklist=False):
        self.name = name
        self.company = company
        self.pay = pay
        self.in_list = in_list
        self.in_blacklist = in_blacklist
        
    def employee_status(self):
        if self.in_list and self.in_blacklist:
            return "employed"
        elif not self.in_list:
            return "visitor"
        else:
            return "intruder"
        
# employee1 = Employee(name="Calvin Kiptoo", company="Watu credit", pay="30000", in_list=True, in_blacklist=True)
# print(f"{employee1.name} working at {employee1.company} earning {employee1.pay} is {employee1.employee_status()}")
# employee2 = Employee(name="Leornard Kiptoo", company="Watu credit", pay="25000", in_list=False, in_blacklist=True)
# print(f"{employee2.name} working at {employee2.company} earning {employee2.pay} is {employee2.employee_status()}")
employee3 = Employee(name="Onesmus", company="Hiline", pay="20000", in_list=True, in_blacklist=False)
print(f"{employee3.name} working for {employee3.company} earning {employee3.pay} is an  {employee3.employee_status()}")