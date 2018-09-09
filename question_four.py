# Using any object oriented language, please define a class model to implement the
# following specification:
# A company has a staffing model which includes Employees, Contractors, and Temporaries. We want
# an object model which implements this structure. The expected behavior for the classes is


class Employee(object):
    """ Employee class
    """
    def __init__(self, first_name, last_name, pay_rate, vacation):
        """
        Employee class attributes
        :param str first_name:
        :param str last_name:
        :param float pay_rate:
        :param int vacation:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.pay_rate = pay_rate
        self.vacation = vacation

    def get_name(self):
        return "Employee Name: {0}, {1}".format(self.last_name, self.first_name)

    def get_pay_rate(self):
        return "Hourly pay rate: " + str(self.pay_rate)

    def get_yearly_vacation(self):
        return "Yearly Vacation : " + str(self.vacation)


class Contractor(Employee):
    """Contractor class"""
    __vacation = 0

    def __init__(self, first_name, last_name, pay_rate, agency_name):
        """
        Contractor class attributes
        :param str first_name:
        :param str last_name:
        :param float pay_rate:
        :param str agency_name:
        """
        super().__init__(first_name, last_name, pay_rate, vacation=self.__vacation)
        self.agency_name = agency_name

    def get_name(self):
        return "Employee Name: {0}, {1} [C]".format(self.last_name, self.first_name)

    def get_agency(self):
        return "Agency Name: " + self.agency_name


class Temporary(Contractor):
    """
    Temporary class attributes
    """
    def __init__(self, first_name, last_name, pay_rate, agency_name):
        """
        Temprary class attributes
        :param str first_name:
        :param str last_name:
        :param float pay_rate:
        :param str agency_name:
        """
        super().__init__(first_name, last_name, pay_rate, agency_name)

    def get_name(self):
        return "Employee Name: {0}, {1} [T]".format(self.last_name, self.first_name)


emp = Employee('mahesh', 'prasad', 500, 20)
print(emp.get_name(), emp.get_pay_rate(), emp.get_yearly_vacation())

contr = Contractor('vivek', 'kumar', 400, 'Gemalto')
print(contr.get_name(), contr.get_pay_rate(), contr.get_yearly_vacation(), contr.get_agency())

temp = Temporary('ranjan', 'kumar', 200, 'SafeNet')
print(temp.get_name(), temp.get_pay_rate(), temp.get_yearly_vacation(), temp.get_agency())
