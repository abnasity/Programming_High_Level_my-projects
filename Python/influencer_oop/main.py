class Student:
    def __init__(self, name, age, id, is_admin=False, is_logged_in=False):
        self.name = name
        self.age = age
        self.id = id
        self.is_admin = is_admin
        self.is_logged_in = is_logged_in
        
    def influencer_status(self):
        if self.is_admin and self.is_logged_in:
            return "Dashboard"
        elif self.is_logged_in:
            return "Login page"
        else:
            return "Newsfeed"
        
        
        
influencer = Student(name="Enock", age=23, id=40498987, is_admin=False, is_logged_in=False)
print(f"{influencer.name} aged {influencer.age} has an id number of {influencer.id} is directed to {influencer.influencer_status()}")
        
        