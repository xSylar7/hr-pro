class Employee:
   #Employee class here
    def __init__(self, name, age, salary, employment_years):
         self.name = name
         self.age = age
         self.salary =salary
         self.employment_years = employment_years

    def get_annual_salary(self,salary):
        return self.salary * 12

    def __str__(self):
         return f"Employee name is {self.name} his age {self.age} his salary {self.salary} his years of employement {self.employment_years}"

employee_1 = [Employee("Mohammad", 30,2000,6)]
# employee1 =  --> Test for the employee class
# print (employee_1[0])

class Manager(Employee):
    #Manager class here
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
         super().__init__(name, age, salary, employment_years)
         self.bonus_percentage = bonus_percentage
         
    def get_bonus(self, bonus_percentage, salary):
        return self.bonus_percentage * self.salary

    def __str__(self):
         return f"Manager name is {self.name} his age {self.age} his salary {self.salary} his years of employement {self.employment_years} his bonus {self.bonus_percentage}%"

manager_q = [Manager("Qassem", 28, 5000, 7, 90)]
print (manager_q[0])

def show_options ():
    options = ["Show Employees", "Show Managers", "Add an Employee", "Add a manager"]
    for index, option in enumerate(options,1):
        print (index, option)

# show_options() ---> test for show options

def get_user_option():
    show_options ()
    user_option = int(input ("What Would you like to do?"))

    if user_option == 1:
        print (employee_1[0])
    elif user_option == 2:
        print (manager_q[0])
    elif user_option == 3:
        user_input = []
        user_name = input ()
        # input (Employee("what is your name", "whats your age", "whats your")) ---> Failed test


get_user_option()

def main():
	# main code here

    if __name__ == '__main__':
	    main()
