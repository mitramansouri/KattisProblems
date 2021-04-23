# objective : bundling data and functionality 
# instance / obj 
# method / attr

# scopes and namespaces

#Enclosing Namespaces

# namespaces and scppes of them
# builtin :containing functions such as abs(), and built-in exception names 
# the global names in a module
# local names in a function 

# scopes 
# x = 98.6
# def scope_test():
#     def do_local():
#         spam = "local spam"
#         print('In do local:' , spam)

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"
#         print('In global Spam:' , spam)


#     spam = "test spam"
#     print('Before assignments:' ,spam)
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'
# # instantiation
# m = MyClass()

# print(m.i, m.f(), sep='\n')

# m.i = 54321
# print(m.i, m.f(), sep='\n')

# initialize 
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

#     def conjugate(self):
#         self.r = self.r
#         self.i = -self.i 
        
#     def __str__(self):
#         return str(self.r) + '+(' + str(self.i) + ')j'

# complex_num = Complex(5, -7)
# print(complex_num)
# complex_num.conjugate() # conjugate(complex_num) 
# print(complex_num)

# class Dog:

#     wrong_tricks = []

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # creates a new empty list for each dog

#     def add_trick(self, trick):
#         self.tricks.append(trick)


# golden_retiver = Dog('Gold')
# # golden_retiver.wrong_tricks.append('plays catch')
# golden_retiver.add_trick('plays catch ')

# chiwawa = Dog('Jake')
# chiwawa.add_trick('rolls back')
# # chiwawa.wrong_tricks.append('rolls back ')

# print(*golden_retiver.tricks)
# # print(*golden_retiver.wrong_tricks)
# # print(*chiwawa.wrong_tricks)
# print(*chiwawa.tricks)

# Inheritance

# class Employee:

#     raise_amt = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)

# emp_1 = Employee('Mitra', 'Mansouri', 6000)
# print(emp_1.email , emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


# class Developer(Employee):
#     # adding more info that parent has
#     raise_amt = 1.10
#     def __init__(self, first, last, pay, prog_lang):
#         self.raise_amt = 1.10
#         # self.first = first
#         # self.last = last
#         # self.email = first + '.' + last + '@email.com'
#         # self.pay = pay
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
#     # pass

# emp_1 = Developer('Mitra', 'Mansouri', 6000 , 'Python')
# emp_2 = Employee('Mia', 'Mansouri', 6000)
# emp_1.apply_raise()
# emp_2.apply_raise()
# print(emp_1.fullname() , emp_1.pay, sep='\n')
# print(emp_2.fullname(), emp_2.pay, sep='\n')

# class Manager(Employee):
#     raise_amt = 1.20
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees

#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())


# emp_3 = Manager('Manager', 'Test', 8000, [emp_1, emp_2])
# emp_3.print_emps()
# dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
# dev_2 = Employee('Test', 'Employee', 60000)

# print(help(Developer))
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(dev_1.email, dev_1.prog_lang, sep='\n')


# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_2)

# mgr_1.print_emps()
# isinstance(class1 , class2)
# issubclass(child,parent)

class Intv:
    def __init__(self, x):
        self.x = x
    
    def __add__(self, other):
         
        return self.x + other.x

    def __str__(self):
        return "{x}".format(x=self.x)

# firts = Intv('s')
# print(firts)
# firts1 = Intv(6)
# print(firts + firts1)  # x.add(y)


# try:
#     firts = Intv('s')
#     print(firts)
#     firts1 = Intv(6)
#     print(firts + firts1)  # x.add(y)

# except TypeError as x:
#     print(f"THIS YOUR ERROR:\n {x}")
#     ...
# except Exception as error:
#     print(f"This asda{error} ")


def add_number(x):
    return x +2


import unittest
from datetime import datetime
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n - 1) * n
        
class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(add_number(2), 4)

    def test7(self):
        tic = datetime.now()
        add_number(100)
        tac = datetime.now()
        self.assertLessEqual((tac - tic).seconds, 1)
        
    def test_factorial(self):
        self.assertEqual(factorial(5), 121)
unittest.main()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial(n - 1) * n
        
