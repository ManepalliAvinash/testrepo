class Employee:
    Emp_raise=1.04
    Emp_count=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first+"."+last+"@company.com"

        Employee.Emp_count+=1


    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def pay_raise(self):
        return (self.pay * self.Emp_raise)

    @classmethod
    def set_emp_raise(cls,new_raise):
        cls.Emp_raise=new_raise

    """@classmethod
    def from_string(cls,new_string):
        first,last,pay=new_string.split("-")
        return cls(first,last,pay)


    @staticmethod
    def check_weekday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True"""

emp1=Employee("groot","green",10000)
emp2=Employee("hulk","green",20000)
"""print(emp1.Emp_raise)
emp1.set_emp_raise(2.5)
print(emp1.Emp_raise)
print(emp1.pay_raise())"""
"""print(Employee.Emp_raise)
Employee.set_emp_raise(3.2)
print(Employee.Emp_raise)"""

"""emp3="jhon-dhes-2000"
empx=Employee.from_string(emp3)
print(empx.fullname())
import datetime
new_date=datetime.date(2024,2,5)
print(Employee.check_weekday(new_date))"""

num=[1,2,3,4,5,6,7,8,9]

"""def even(n):
    return n%2==0

even_lst=list(filter(even,num))
print(even_lst)
"""
"""import array as arr
arr1=arr.array('i',[1,2,3,4,5])
arr2=arr.array('i',[1,2,1,4,5])"""

from numpy import *
#arr1=array([1,2,3,4,5])
"""arr2=arr1.view()
arr1[0]=6
print(arr1)
print(arr1)
print(id(arr1))
print(id(arr2))"""
"""
arr2=arr1.copy()
arr1[0]=10
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))"""

