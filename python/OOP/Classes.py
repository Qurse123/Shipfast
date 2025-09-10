class Employee: ## This is a class 

    def __init__(self, first, last, pay): ## this is a method
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first + "." + last + "@company.com"

    def fullname(self): ## this is a method
        return  "\n" + self.first + " " + self.last



emp_1 = Employee("first1", "last1", "10")
emp_2 = Employee("first2", "last2", "20")

print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())


emp_1.fullname() ## here we call the instance emp_1 and the method fullname
Employee.fullname(emp_1) ## When call the class employee then the method fullname but it needs an instance in this case this is emp_1
## both of these preform the same thing
