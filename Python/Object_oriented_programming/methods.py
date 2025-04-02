
#Instance,class and static methods

class Example:
    class_attr = "I am a class attribute"

    def __init__(self, value):
        self.value = value  # Instance attribute

    def instance_method(self):  # Uses self
        return f"Instance method: {self.value}"

    @classmethod
    def class_method(cls):  # Uses cls
        return f"Class method: {cls.class_attr}"

    @staticmethod
    def static_method():  # No self or cls
        return "Static method called"

obj = Example("Hello")

print(obj.instance_method())  # ✅ Uses instance attribute
print(Example.class_method()) # ✅ Uses class attribute
print(Example.static_method()) # ✅ Independent utility method
