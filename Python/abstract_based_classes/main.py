
# In Python, we use ABC to create abstract classes. Abstract classes have methods declared but not defined; we mark them with @abstractmethod. For example, a Shape abstract class might have area and perimeter. Concrete classes like Circle and Square inherit from Shape and define these methods according to their shapes, making code more flexible.










class Students:
    
    def enroll(self):
        pass
    def graduate(self):
        pass
    
class Graduates(Students):
        def enroll(self):
            return "Enrolling in a graduate program"
            
        def graduate(self):
            return "graduating from enrolled program"
vague_student = Graduates()
print(vague_student.graduate())