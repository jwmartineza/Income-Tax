#!/usr/bin/env python3
#Income Tax Calculator By Jonathan Martinez
# 1 -  Customer Request input
gross_income = float(input("Enter the gross income: "))
num_dependents = int(input("Enter the number of dependents: "))

# 2 -  Calculate taxable income
standard_deduction = 10000
additional_deduction_per_dependent = 3000
total_deduction = standard_deduction + (num_dependents * additional_deduction_per_dependent)
taxable_income = gross_income - total_deduction

# 3 -  Calculation of income tax by IRS
tax_rate = 0.20
income_tax = taxable_income * tax_rate

# 4 -  Display the result, sep='' will let $ sign next to the result.
print("The income tax is $", format(income_tax, ".1f"), sep='')