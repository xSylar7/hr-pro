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
         pass

class Manager(Employee):
    #Manager class here
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
         super().__init__(name, age, salary, employment_years)
         
    def get_bonus(self, bonus_percentage, salary):
        return self.bonus_percentage * self.salary
        
def main():
	# main code here

if __name__ == '__main__':
	main()
