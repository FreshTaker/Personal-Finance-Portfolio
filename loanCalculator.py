"""Loan Calculator
    Can calculate:
    * number of monthly payments
    * annuity monthly payment amount
    * credit principal
    * differentiated payments (constant pay down of principal)

Can be called by command line using arguments.
"""

import argparse
import math


def number_payments(A, i, P):
    """Finding the number of payments using:
    A = annuity payment
    P = credit principal
    i = nominal (monthly) interest rate (float, not a percentage)
    Returns formatted "It will take Y years and X months" string.
    """
    A = int(A)
    P = int(P)
    i = float(i) / (100 * 12)
    num_payments = math.ceil(math.log(A / (A - (i * P)), (1 + i)))
    # Convert to years and months
    years = num_payments // 12
    months = num_payments % 12
    if years == 0:
        string_y = ''
    elif years == 1:
        string_y = f'{years} year'
    else:
        string_y = f'{years} years'

    if months == 0:
        string_m = ''
    elif months == 1:
        string_m = f'{months} month'
    else:
        string_m = f'{months} months'

    if (len(string_y) > 0) and (len(string_m) > 0):
        res = string_y + ' and ' + string_m
    else:
        res = string_y + string_m

    overpayment = (num_payments * A) - P
    res = f'It will take {res} to repay this credit\nOverpayment = {overpayment}'
    return res


def annuity_payment(P, n, i):
    """Finding the annuity payment (monthly) using:
    P = credit principal
    n = number of payments (months)
    i = nominal (monthly) interest rate (float, not a percentage)
    Returns formatted string"""
    P = int(P)
    n = int(n)
    i = float(i) / (100 * 12)
    A = math.ceil(P * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
    overpayment = (n * A) - P
    res = f'Your annuity payment = {A}!\nOverpayment = {overpayment}'
    return res


def credit_principal(A, n, i):
    """Finding the credit principal using:
    A = annuity payment
    n = number of payments (monthly)
    i = nominal (monthly) interest rate (float, not a percentage)
    Returns formatted string.
    """
    A = float(A)
    n = int(n)
    i = float(i) / (100 * 12)
    P = math.floor(A / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
    overpayment = (n * A) - P
    res = f'Your credit principal = {P}!\nOverpayment = {overpayment}'
    return res


def diff_payments(P, n, i):
    """Finding the differentiated payment using:
    P = credit principal
    n = number of payments (months)
    i = nominal (monthly) interest rate (float, not a percentage)
    Returns formatted string

    A differentiated payment schedule is where part of the payment reduces the credit principal is constant.
    """
    P = int(P)
    n = int(n)
    i = float(i) / (100 * 12)
    subtotal = 0
    res = ''
    for m in range(1, n + 1):
        D_m = math.ceil((P / n) + i * (P - (P * (m - 1) / n)))
        res = res + f'Month {m}: payment is {D_m}\n'
        subtotal += D_m

    overpayment = subtotal - P
    string_overpayment = f'\nOverpayment = {overpayment}'
    res = res + string_overpayment
    return res


def credit_calc():
    print('What do you want to calculate?')
    print('type "n" for number of monthly payments,')
    print('type "a" for annuity monthly payment amount,')
    print('type "p" for credit principal,')
    print('type "d" for differentiated payments:')
    user_input = input()

    # Prompts:
    prompt_principal = 'Enter the credit principal: '
    prompt_payment = 'Enter the monthly payment: '
    prompt_interest = 'Enter the credit interest: '
    prompt_periods = 'Enter the number of periods: '

    if user_input == "n":
        # Number of monthly payments
        input_principal = input(prompt_principal)
        input_payment = input(prompt_payment)
        input_interest = input(prompt_interest)
        string_n = number_payments(input_payment, input_interest, input_principal)
        print(string_n)

    if user_input == "a":
        # Annuity monthly payment amount
        input_principal = input(prompt_principal)
        input_periods = input(prompt_periods)
        input_interest = input(prompt_interest)
        string_a = annuity_payment(input_principal, input_periods, input_interest)
        print(string_a)

    if user_input == "p":
        # Credit principal
        input_payment = input(prompt_payment)
        input_periods = input(prompt_periods)
        input_interest = input(prompt_interest)
        string_p = credit_principal(input_payment, input_periods, input_interest)
        print(string_p)

    if user_input == "d":
        # Differentiated payments
        input_principal = input(prompt_principal)
        input_periods = input(prompt_periods)
        input_interest = input(prompt_interest)
        string_d = diff_payments(input_principal, input_periods, input_interest)
        print(string_d)

# Define arguments if called by the command line.
parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type of calculation", type=str)
parser.add_argument("--principal", help="principal", type=int)
parser.add_argument("--periods", help="number of periods", type=int)
parser.add_argument("--interest", help="interest rate (float)", type=float)
parser.add_argument("--payment", help="payment amount", type=int)
args = parser.parse_args()
None_count = 0
for arg in vars(args):
    if getattr(args, arg) is None:
        None_count += 1
if None_count == 5:
    # If no arguments given, provide script:
    credit_calc()
elif (None_count > 1) and (None_count < 5):
    print('Incorrect parameters')
elif args.type is None:
    print('Incorrect parameters')
elif args.type == 'diff':
    if args.payment is None:
        print(diff_payments(args.principal, args.periods, args.interest))
    else:
        print('Incorrect parameters')
elif args.type == 'annuity':
    if args.principal is None:
        print(credit_principal(args.payment, args.periods, args.interest))
    elif args.payment is None:
        print(annuity_payment(args.principal, args.periods, args.interest))
    elif args.periods is None:
        print(number_payments(args.payment, args.interest, args.principal))
    elif args.interest is None:
        print('Incorrect parameters')
