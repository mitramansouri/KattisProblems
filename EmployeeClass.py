class Employee:

    def __init__(self, first, last, pay, dept):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.dept = dept

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay)

class Developer(Employee):
    # adding more info that parent has
    def __init__(self, first, last, pay,dept ,skills=None):
        super().__init__(first, last, pay, dept)
        if skills is None:
            self.skills = []
        else:
            self.skills = skills
    # add skill
    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
    
    def print_skill(self):
        for skill in self.skills:
            print('Developer :', self.fullname(),'Skills:' , skill , 'Department :' , self.dept, sep='\n')

emp_1 = Employee('Sina', 'Something', 6000, 'Comp')
dev_1 = Developer('Mitra', 'Mansouri', 2000, 'Comp', ['Python'])
dev_1.print_skill()