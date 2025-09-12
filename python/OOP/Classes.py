class Employee: ## This is a class 

    num_of_emps = 0 
    raise_ammount = 1.04 ## class variable
    
    
    def __init__(self, first, last, pay): ## this is a method the init method runs everytime we create a new employee
        self.first = first
        self.last = last 
        self.pay = pay 
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps +=1 ## we use employee instead of self because we cant think of any use case where we would want a differnt number of empolyees for any 1 instance

    def fullname(self): ## this is a method
        return  "\n" + self.first + " " + self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_ammount) # This is more diffuclt to change as it is defined by a class variable
    #   self.pay = int(self.pay * self.raise_ammount) ## this can be changed more easily as we are using the self attribute in the instance
# hence if we use self.raise_ammount then this allows us to later change emp_1 raise ammoumt


emp_1 = Employee("first1", "last1", "10")
emp_2 = Employee("first2", "last2", "20")

##print(emp_1.email)
##print(emp_2.email)
##print(emp_2.fullname())


##emp_1.fullname() ## here we call the instance emp_1 and the method fullname
##Employee.fullname(emp_1) ## When call the class employee then the method fullname but it needs an instance in this case this is emp_1
## both of these preform the same thing

print(Employee.num_of_emps)