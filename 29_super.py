class Person1:
    def __init__(self):
        print("class 1")
    
    def greet(self):
        print("Good Morning")


class Person2(Person1):
    def __init__(self):
        super().__init__()
        super().greet()
        print("class 2")


class Person3(Person2):
    def __init__(self):
        super().__init__()
        print("class 3")


p3 = Person3()
