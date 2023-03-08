class Person:
    def job(self):
        print("I am a person")

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        print('{} {}'.format(self.first, self.last))


class Programmer(Employee,Person):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def get_prog_lang(self):
        print(self.prog_lang)


mohammed = Employee("mohammed", "obaid", 50000)
mohammed.fullname()
obaid = Programmer("obaid", "mohammed", 60000, "py thon")
obaid.fullname()
obaid.get_prog_lang()
obaid.job()

