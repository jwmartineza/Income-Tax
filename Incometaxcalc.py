#!/usr/bin/env python3

#Income Tax Calculator By Jonathan Martinez
# 1 -  Customer Request input
gross_income = float(input("Enter the gross income: "))
num_dependents = int(input("Enter the number of dependents: "))

# 2 -  Calculate taxable income
# Total Deduction = standard deduction + (number of dependents x additional deduction per dependent)
# Taxable Income = Gross Income - Total Deduction
standard_deduction = 10000
addit_deduc_per_dep = 3000
total_deduction = standard_deduction + (num_dependents * addit_deduc_per_dep)
taxable_income = gross_income - total_deduction

# 3 -  Calculation of income tax
# Income tax = Tax Income x Tax Rate
tax_rate = 0.20
income_tax = taxable_income * tax_rate

# 4 -  Display the result, sep='' will let $ sign next to the result.
print("The income tax is $", format(income_tax, ".1f"), sep='')