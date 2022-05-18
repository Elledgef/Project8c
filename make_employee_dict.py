# Author: Faith Elledge
# Gritbuhuser: Elledgef
# Date: 5/18
# Description: Private data members for an employees name, ID number, Salary and email address

class Employee:
    def __init__(self, name, id, salary, email_address):
        self.id = id
        self.name = name
        self.salary = salary
        self.email_address = email_address

    def make_employee_dict(names,ids, salaries, emails):
        employee_dict = {}
        for i in range(len(names)):
            emp= Employee(names[i], ids[i], salaries[i], emails[i])
            employee_dict[ids[i]] = emp
        return employee_dict



