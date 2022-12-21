'''
employee_records.py :

By Will Colvill

12/5/19
'''

def getEmployeeInfo():
    emp_ident = input("What is your employee ID: "), '\n'
    emp_name = input("What is your name: "), '\n'
    hours_worked = int(input("How many hours have you worked this week: ")), '\n'
    pay_rate = float(input("What is your hourly pay rate (do not include $ sign): ")), '\n'
    return emp_ident, emp_name, hours_worked, pay_rate

def calcGrossPay(hours, pay_rate):
    if hours > 40:
        weekly_pay = (pay_rate * 40) + ((hours - 40)*pay_rate)
    else:
        weekly_pay = pay_rate * hours
    return weekly_pay

def displayPayStatement(emp_id, name, hours, pay_rate, weekly_pay, total_emp, total_hours, total_pay):
    print("Employee ID         Employee Name       Hours Worked        Gross Pay           ")
    print('%-20s' % str(emp_id) + '%-20s' % str(name) + '%-20s' % str(hours) + '%-20s' % str(weekly_pay))
    print('--------------------------------------------------------------------------------')
    print("Total Employees:", str(total_emp))
    print("Total Hours Worked:", str(total_hours))
    print("Total Gross Pay:", "$" + str(total_pay))

def main():
    enter = 1
    emp_id = ''
    name = ''
    total_pay = 0
    total_emp = 0
    total_hours = 0
    hours = 0
    pay_rate = 0
    weekly_pay = 0
    emp_ident = ''
    emp_name = ''
    hours_worked = 0
    while enter == 1:
        getEmployeeInfo()
        calcGrossPay(hours, pay_rate)
        total_hours += hours
        total_pay += weekly_pay
        total_emp += 1
        emp_id = emp_id, '\n', emp_ident
        name = name, '\n', emp_name
        hours = hours, '\n', hours_worked

        enter = int(input("Press 1 for another employee or 2 to Finish"))
    displayPayStatement(emp_id, name, hours, pay_rate, weekly_pay, total_emp, total_hours, total_pay)

main()

