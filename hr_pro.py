class Employee:
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_working_years(self):
        return date.today().year - int(self.employment_year)

    def __str__(self):
        return "Name: %s, Age: %s, Salary: %s, Working Years: %d" % (self.name, self.age, self.salary, self.get_working_years())

class Manager(Employee):
    pass
        
def main():
	pass

if __name__ == '__main__':
	main()
