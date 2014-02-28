import csv
import sys


with open('npremployees.csv', "rU") as npr_employees:
	employees = csv.DictReader(npr_employees)
	dict = employees

	for individual in employees:
		values = individual.values()
		print values
		

with open('social22814.csv', "rU") as employee_social_survey:
  	survey = csv.DictReader(employee_social_survey)
	dict = survey

 	for employee in survey:
		values = employee.values()
		#print values

	#for employee in survey:
		text = values[4]
		print text

	#if employee.values() == individual.values():
	#	print "Hooray!"
	#else:
	#	print "Back to the drawing board Kramer!"







#employees_plus_survey = file('results.csv', 'w')

#master_document = csv.writer(employees_plus_survey)


