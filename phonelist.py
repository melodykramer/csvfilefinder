import csv
import sys


#this opens up a list of all npr employees and puts their info into dictionary

with open('npremployees.csv', "rU") as npr_employees:
	employees = csv.DictReader(npr_employees)
	for person in employees:
		print person

#this opens up a list of all npr employees who filled out a survey and puts their info into dictionary

with open('social22814.csv', "rU") as employee_social_survey:
	survey = csv.DictReader(employee_social_survey)
	for employee in survey:
		print employee
		
#Here's where I'm screwing up. I want to say "If the string in row 12 of the second table equals the string in row 18 of the first 
#table, then print yay. I know I'm counting correctly (I started counting at 0.) What am I doing wrong?
	
	#	if employees[12] == person[18]:
	#		print "yay"
	#	else:
	#		print "nope"


#employees_plus_survey = file('results.csv', 'w')

#master_document = csv.writer(employees_plus_survey)


employee_social_survey.close()
npr_employees.close()
#employees_plus_survey.close()
