class Employee:
    company = "google"
    salary = 0

    def getSalary(self):
        print(
            f"The salary of employee working in {self.company} is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning, Sir")  


harry = Employee()
harry.salary = 100000
harry.getSalary()
harry.greet()
