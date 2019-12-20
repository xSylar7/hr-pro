import io
from contextlib import redirect_stdout
from unittest.mock import patch
import unittest
import hr_pro
from datetime import date


class ClassesTest(unittest.TestCase):

	def test_employee_class(self):
		employee = hr_pro.Employee("laila", 44, 333, 2000)
		self.assertEqual("laila", employee.name)
		self.assertEqual(44, employee.age)
		self.assertEqual(333, employee.salary)
		self.assertEqual(2000, employee.employment_year)

	def test_get_working_years(self):
		employee = hr_pro.Employee("laila", 44, 333, 2000)
		years = date.today().year - employee.employment_year
		self.assertEqual(years, employee.get_working_years())

	def test_manager_class(self):
		manager = hr_pro.Manager("name", 33, 4000, 2006, .3)
		self.assertEqual("name", manager.name)
		self.assertEqual(33, manager.age)
		self.assertEqual(4000, manager.salary)
		self.assertEqual(2006, manager.employment_year)
		self.assertEqual(.3, manager.bonus_percentage)

	def test_manager_get_working_years(self):
		manager = hr_pro.Manager("name", 33, 4000, 2006, .3)
		years = date.today().year - manager.employment_year
		self.assertEqual(years, manager.get_working_years())

	def test_get_bonus(self):
		manager = hr_pro.Manager("name", 33, 4000, 2006, .3)
		self.assertEqual(.3*4000, manager.get_bonus())


class FunctionTesting(unittest.TestCase):
	def setUp(self):
		self.response = io.StringIO()
		self.employees = [
			hr_pro.Employee("laila1", 44, 100, 2003), 
			hr_pro.Employee("laila2", 14, 200, 2012), 
			hr_pro.Employee("laila3", 54, 300, 2009)
		]
		self.managers = [
			hr_pro.Manager("name1", 34, 400, 2000, .5),
			hr_pro.Manager("name2", 23, 5000, 2016, 1),
			hr_pro.Manager("name3", 3, 4050, 2019, .3)
		]

	def test_one_create_and_print_employees(self):
		user_input = [3,self.employees[0].name, self.employees[0].age, self.employees[0].salary, self.employees[0].employment_year,1,5]
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				hr_pro.main()
				self.assertTrue(self.employees[0].name in self.response.getvalue())

	def test_multiple_create_and_print_employees(self):
		user_input = []
		for employee in self.employees:
			user_input.extend([3, employee.name, employee.age, employee.salary, employee.employment_year])
		user_input.extend([1,5])
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				hr_pro.main()
				for employee in self.employees:
					self.assertTrue(employee.name in self.response.getvalue())

	def test_one_create_and_print_manager(self):
		user_input = [4,self.managers[0].name, self.managers[0].age, self.managers[0].salary, self.managers[0].employment_year,self.managers[0].bonus_percentage,2,5]
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				hr_pro.main()
				self.assertTrue(self.managers[0].name in self.response.getvalue())

	def test_multiple_create_and_print_managers(self):
		user_input = []
		for manager in self.managers:
			user_input.extend([4, manager.name, manager.age, manager.salary, manager.employment_year, manager.bonus_percentage])
		user_input.extend([2,5])
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				hr_pro.main()
				for manager in self.managers:
					self.assertTrue(manager.name in self.response.getvalue())

	def testـonly_employees_printing(self):
		user_input = []
		for manager in self.managers:
			user_input.extend([4, manager.name, manager.age, manager.salary, manager.employment_year, manager.bonus_percentage])
		for employee in self.employees:
			user_input.extend([3, employee.name, employee.age, employee.salary, employee.employment_year])
		user_input.extend([1,5])
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				hr_pro.main()
				for manager in self.managers:
					self.assertFalse(manager.name in self.response.getvalue())
				for employee in self.employees:
					self.assertTrue(employee.name in self.response.getvalue())

	def testـonly_managers_printing(self):
		user_input = []
		for manager in self.managers:
			user_input.extend([4, manager.name, manager.age, manager.salary, manager.employment_year, manager.bonus_percentage])
		for employee in self.employees:
			user_input.extend([3, employee.name, employee.age, employee.salary, employee.employment_year])
		user_input.extend([2,5])
		with redirect_stdout(self.response):
			with patch('builtins.input', side_effect=user_input):
				hr_pro.main()
				for manager in self.managers:
					self.assertTrue(manager.name in self.response.getvalue())
				for employee in self.employees:
					self.assertFalse(employee.name in self.response.getvalue())



if __name__ == '__main__':
	unittest.main()

