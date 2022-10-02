class Employee:
   #Employee class here
    def __init__(self, name, age, salary, employment_years):
         self.name = name
         self.age = age
         self.salary =salary
         self.employment_years = employment_years

    def get_annual_salary(self):
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
         
    def get_bonus(self):
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
        employee_input = Employee(input ("Enter your name"),input ("Enter your age"),input ("Enter your salary"),input ("Enter your years of experince"))
        print (employee_input)

        #----------Extreem Method but it works --------------
        # employee_user_input = []
        # employee_name = input ("Enter your name")
        # employee_age = input ("Enter your age")
        # employee_salary = input ("Enter your salary")
        # employee_years = input ("Enter your years of experince")
        # employee_user_input.extend([employee_name,employee_age,employee_salary,employee_years])
        # print (employee_user_input)


    elif user_option == 4:
        manager_input = Manager(input ("Enter your name"),input ("Enter your age"),input ("Enter your salary"),input ("Enter your years of experince"), input ("Enter your bonus %"))
        print (manager_input)




        # ----------Extreem Method but it works --------------
        # manager_user_input = []
        # manager_name = input ("Enter your name")
        # manager_age = input ("Enter your age")
        # manager_salary = input ("Enter your salary")
        # manager_years = input ("Enter your years of experince")
        # manager_bonus = input ("Enter your bonus")
        # manager_user_input.extend([manager_name,manager_age,manager_salary,manager_years,manager_bonus])
        # print (manager_user_input)

        # input (Employee("what is your name", "whats your age", "whats your")) ---> Failed test


get_user_option()

def main():
	# main code here

    if __name__ == '__main__':
	    main()
