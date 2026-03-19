#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 17:36:30 2026

@author: izzy.araojo
"""

# Problem Set 2
# Name: Izzy Araojo
# Collaborators: N/a
#Time spent on A-1: 20 mins
#Time spent on A-2: 50 mins
#Time spent on B-1: 40 mins

#goal: find number of months to save up for down payment
#down payment = total cost of home * down payment percent
#semi annual = every 6 months

yearly_salary = float (input( "Enter Starting Yearly Salary: "))
portion_saved = float (input( "Enter Portion of Salary to be Saved: "))
cost_of_dream_home = float(input("Enter Cost of Dream Home: "))
semi_annual_raise = float(input( "Enter Semi Annual Raise: "))

portion_down_payment = 0.25
r = 0.05
amount_saved = 0.0
months = 0
months_since_raise = 0
down_payment=cost_of_dream_home * portion_down_payment


while amount_saved < down_payment:
    monthly_return = amount_saved * (r/12)
    monthly_salary = yearly_salary / 12
    savings = portion_saved * monthly_salary
    amount_saved = amount_saved + (savings) + monthly_return
    months = months + 1
    months_since_raise = months_since_raise+1
    if months_since_raise == 6:
        yearly_salary = yearly_salary + (yearly_salary * semi_annual_raise)
        months_since_raise = 0
#n=n+1
#n is number of months

print ("Number of Months:",months)