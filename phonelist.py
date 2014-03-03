import csv


#opens spreadsheet of every NPR employee

with open('npremployees.csv', "rU") as npr_employees:

#puts all of their information into a dictionary

       employees = csv.DictReader(npr_employees)

       all_employees = {}

       total_employees = {}


#loops through all of the employees and assigns them a unique value of their extension

       for employee in employees:

               all_employees[employee['Extension']] = employee


#opens up spreadsheet of NPR employees who filled out a survey

with open('social22814.csv', "rU") as social_employees:

#puts all of their information into a dictionary

       social_employee = csv.DictReader(social_employees) 


#if the employee appears in the master list, print out their information. 
#This lets us know which employees should have information added to the master list entry.

       for row in social_employee:

          # total_employees[row['Extension']]['Instagram'] = row

             #  print total_employees.get(row['Extension'], None)
            	

               print all_employees.get(row['Extension'], None)


