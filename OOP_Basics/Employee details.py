'''Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))
'''

'''

list=[]


'''

class Employee:
    def __init__(self):        
        self.employees =[]
        
    def add_employee(self, Name , emp_id ,salary, working_hour , dept): 
        self.name = Name
        employee = [Name , str(emp_id) , self.working_hour(salary,working_hour), self.assign_department(dept)]
        self.employees.append(employee)
        print(f'Employee {Name} is Updated\n')       
        
    def working_hour(self,salary,work_hour):
        if work_hour > 50:
            overtime= work_hour-50
            overtime_amount = (overtime * (salary / 50)) 
            return str(int(salary+overtime_amount))
    
    
    def assign_department(self, dept):
        self.dept = dept
        
    def print_employee_details(self):
        print('Name     Emp_ID     Salary    Dept\n')
        for employee in self.employees:
            print(f'{employee[0]}    {employee[1]}    {employee[2]}    {employee[3]}')
        print()
employee = Employee()

employee.add_employee('Vishva', 7552003, 50000 , 52 , 'CSE' )
employee.add_employee('Vis', 5552023, 45000 , 60 , 'BME' )
employee.add_employee('vis', 1552203, 60000 , 50 , 'Civil' )
employee.add_employee('avhsiv', 3452003, 43000 , 45 , 'Mech' )
employee.add_employee('skd', 1342003, 56000 , 53 , 'CSE' )

employee.print_employee_details()