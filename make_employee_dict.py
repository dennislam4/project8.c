# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/22/2022
# Description: A class that contains employee's name, ID_number, salary, and email_address.
# Also contains a funtion that take parameters a list of names, list of ID numbers, list of
# salaries and a list of emails. The function creates a employee objects and  returns a dictionary
# where the key is the ID number and the value is the employee objects created.

class Employee:
    """
    Represents an employee's personal information with their name, ID number, salary and email.
    """
    def __init__(self, name, id_number, salary, email_address):
        """Initializes employee's personal information. """
        self._name = name
        self._id_number = id_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """Returns the name of employee."""
        return self._name

    def get_ID_number(self):
        """Returns ID number of employee."""
        return self._id_number

    def get_salary(self):
        """Returns salary of employee."""
        return self._salary

    def get_email_address(self):
        """Returns the e-mail address of employee."""
        return self._email_address


def make_employee_dict(names, ids, sals, emails):
    """
    Function that creates employee objects and adds it to a dictionary where employee ID
    number is the key and value is the created employee object.
    """
    emp_dic = {}
    for data in range(len(names)):
        employee = Employee(names[data], ids[data], sals[data], emails[data])
        emp_dic[ids[data]] = employee
    return emp_dic
