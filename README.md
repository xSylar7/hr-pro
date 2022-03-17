# Treehouse Prerequisites:

Finish the following chapters/steps from [this course](https://teamtreehouse.com/library/objectoriented-python-2) on treehouse:

- Chapter "**Instant Objects**":  All steps
- Chapter "**Inheritance**":  Up-to and including "**Super!**"

---

# Fork & Clone

Fork and clone [this repository](https://github.com/JoinCODED/hr-pro) in your `python` directory.

---

# Task 

In this task you'll be creating the HR system for a company. This company has two types of employees: normal employees and managers.

The following example assume the current year is 2019.

```
Welcome to HR Pro 2019
Options:
	1. Show Employees
	2. Show Managers
	3. Add An Employee
	4. Add A Manager
	5. Exit

What would you like to do? 3
-----------------
Name: shosho
Age: 24
Salary: 666
Employement year: 2018
Employee added succesfully

Options:
	1. Show Employees
	2. Show Managers
	3. Add An Employee
	4. Add A Manager
	5. Exit

What would you like to do? 1
-----------------
Employees

Name: shosho, Age: 24, Salary: 666, Working Years: 1
-----------------

Options:
	1. Show Employees
	2. Show Managers
	3. Add An Employee
	4. Add A Manager
	5. Exit

What would you like to do? 4
-----------------
Name: sammy
Age: 52
Salary: 4600
Employement Year: 1900
Bonus Percentage: .3
Manager added succesfully

Options:
	1. Show Employees
	2. Show Managers
	3. Add An Employee
	4. Add A Manager
	5. Exit

What would you like to do? 2
-----------------
Managers

Name: sammy, Age: 52, Salary: 4600, Working Years: 119, Bonus: 1380.000000
-----------------

Options:
	1. Show Employees
	2. Show Managers
	3. Add An Employee
	4. Add A Manager
	5. Exit

What would you like to do? 5
```

## Steps:
1. For this task you need to create two classes:
    - `Employee`:
        - `name`
        - `age`
        - `salary`
        - `employment_year`
        - `get_working_years()`
            - `today` - `employment_year`

    - `Manager`:
        - `name`
        - `age`
        - `salary`
        - `employment_year`
        - `bonus_percentage`
        - `get_working_years()`
            - `today` - `employement_date`
        - `get_bonus()`
            - `bonus_percentage` * `salary`
        - Where the `Manager` class inherits from the `Employee` class. 

2. Define a list of `Employee` objects for normal employees, and a list of `Manager` objects for managers.
3. Print the options to the HR employee (the user).
4. If `1` was chosen, print the employees information (the employees list).
5. If `2` was chosen, print the managers information (the managers list).
6. If `3` was chosen, allow the HR employee to add a normal employee to the system (the employees list).
7. If `4` was chosen, allow the HR employee to add a manager to the system (the managers list).
8. If `5` was chosen, stop the program.
9. Push your code.

Hint: The `__str__` method can help you with printing the employees information. You can read about it [here](https://www.journaldev.com/22460/python-str-repr-functions#python--str--and--repr--example)
