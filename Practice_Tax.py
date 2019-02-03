#Nguyen Doan
#1/2/2019
#Computer Science 205
#Homework 2: West Virginia Budget Problem

#3
revenue_growth_rate = 0.01
expenses = 4700000000
initial_revenue = 4200000000
calculated_revenue = 4200000000
years_to_close_shortfall = 0
income = 0

#4
expected_revenue = initial_revenue

while expected_revenue < expenses:
    years_to_close_shortfall += 1
    expected_revenue = initial_revenue*(1+revenue_growth_rate)**years_to_close_shortfall
    if expected_revenue >= expenses:
        print(f'It takes {years_to_close_shortfall} years to close the shortfall, expected revenue is ${expected_revenue:,.2f}.')

#5
calculated_revenue = initial_revenue
revenue_growth_rate = 0.039
while calculated_revenue < expenses:
    years_to_close_shortfall += 1
    calculated_revenue = initial_revenue*(1+revenue_growth_rate)**years_to_close_shortfall
    if calculated_revenue > expenses:
        print(f'It takes {years_to_close_shortfall} years to close the shortfall, expected revenue is ${calculated_revenue:,.2f}.')

#6
income = int(input('Please enter your income: '))
while income == 0:
    income = int(input('Income cannot be 0, please re-enter your income: '))
    
if income < 10000:
    marginal_rate = 0.03
    tax_due = marginal_rate*income
    print(f'User\'s income is ${income:,.0f}, the amount of tax due is ${tax_due:,.0f}, and marginal rate is {marginal_rate:.1%}')
elif income < 25000:
    marginal_rate = 0.04
    tax_due = marginal_rate*income
    print(f'User\'s income is ${income:,.0f}, the amount of tax due is ${tax_due:,.0f}, and marginal rate is {marginal_rate:.1%}')
elif income >= 25000 and income < 40000:
    marginal_rate = 0.045
    tax_due = marginal_rate*income
    print(f'User\'s income is ${income:,.0f}, the amount of tax due is ${tax_due:,.0f}, and marginal rate is {marginal_rate:.1%}')
elif income >= 40000 and income < 60000:
    marginal_rate = 0.06
    tax_due = marginal_rate*income
    print(f'User\'s income is ${income:,.0f}, the amount of tax due is ${tax_due:,.0f}, and marginal rate is {marginal_rate:.1%}')
elif income >= 60000:
    marginal_rate = 0.065
    tax_due = marginal_rate*income
    print(f'User\'s income is ${income:,.0f}, the amount of tax due is ${tax_due:,.0f}, and marginal rate is {marginal_rate:.1%}')
                      
                
#7
'''
a. There are usually two types of expenses: variable and fixed expeneses.
Variable expenses can change based on number of products, services, or employees etc.
In addition, historically speaking, yearly cost is also increasing due to inflatin.
Hence, it is unreasonable to assume that expenses can be held flat.

b. 
As the population of WV becomes older, number of people in the workforce decreases.
This means less tax revenue for WV and less state budget in the future.
'''


