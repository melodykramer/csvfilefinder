import csv


#opens spreadsheet of every NPR employee

with open('npremployees.csv', "rU") as npr_employees:

#puts all of their information into a dictionary

       employees = csv.DictReader(npr_employees)

       all_employees = {}


#loops through all of the employees and assigns them the value of their extension

       for employee in employees:

               all_employees[employee['Extension']] = employee



with open('social22814.csv', "rU") as social_employees:

       social_employee = csv.DictReader(social_employees) 

       for row in social_employee:

               print all_employees.get(row['Extension'], None)

       for employee_new in employees:

   	 	all_employees[employee_new['Extension']]['Instagram'] = employee_new
