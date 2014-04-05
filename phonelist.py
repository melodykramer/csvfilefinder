import csv

# Store all the info about the employees
all_employees = {}
output_headers = []

# First, get all employee record info

with open('npremployees031414.csv', 'rU') as npr_employees:

    employees = csv.DictReader(npr_employees)

    for employee in employees:

        ext = employee['Email']
        all_employees[ext] = employee

    # Add headers from "all employees"

    output_headers.extend(employees.fieldnames)

# Then, get all info from social, and update employee info

with open('testmel.csv', 'rU') as social_employees:


    social_employees = csv.DictReader(social_employees) 
    
    for social_employee in social_employees:
        ext = social_employee['Email']

        # Combine the two dictionaries.
        all_employees[ext] = dict(
                all_employees[ext].items() + social_employee.items()
        )

    # Add headers from "social employees", but don't add duplicate fields
    output_headers.extend(
            [field for field in social_employees.fieldnames
            if field not in output_headers]
    )

# Finally, output the records ordered by extension
with open('output031414l.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(output_headers)

    # Write the new employee rows.  If a field doesn't exist, 
    # write an empty string.
    for employee in sorted(all_employees.values()):
        writer.writerow(
                [employee.get(field, '') for field in output_headers]
        )
