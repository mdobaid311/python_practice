class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    company = "google"
    salary = 0

    def getSalary(self):
        print(
            f"The salary of employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")


harry = Employee("mohammed",1000)
harry.getSalary()
