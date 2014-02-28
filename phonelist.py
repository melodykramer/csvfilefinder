import csv
import sys


#opens up a spreadsheet of every NPR employee
#puts info about them into dictionary

with open('npremployees.csv', "rU") as npr_employees:
	employees = csv.DictReader(npr_employees)
	dict = employees

	for individual in employees:
		values = individual.values()

#prints out their phone extensions which is [5] in a spreadsheet

		extension = values[5]
		print extension

#opens up a spreadsheet of every NPR employee who took a survey
#puts info about them into dictionary		

with open('social22814.csv', "rU") as employee_social_survey:
  	survey = csv.DictReader(employee_social_survey)
	dict = survey

#converts items in dictionary to list

 	for employee in survey:
		values = employee.values()
	
#prints their phone extension, which is [11] in a spreadsheet

		text = values[11]

#I was hoping that this would compare the results from employees to the results from survey
#but this is not the case.

		if text == extension:
			print "Yay!"
		else:
			print "nope!"

#checks to see if phone extension is in both lists. if so, print out employee spreadsheet and adds social handles from list two






#employees_plus_survey = file('results.csv', 'w')

#master_document = csv.writer(employees_plus_survey)



