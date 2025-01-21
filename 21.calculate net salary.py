#calculate net salary

gross_salary=float(input("Enter the gross salary"))
allowance=gross_salary*0.1
deductions=gross_salary*0.03
net_salary = gross_salary+allowance-deductions
print("net salary is",net_salary)
