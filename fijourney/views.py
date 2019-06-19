from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def fijourney_home(request):
    return render(request, 'fijourney/fijourney.html', {'title': 'FIRE Home'})

def result(request):
    age = int(request.POST['age'])
    current_annual_income = float(request.POST['current_annual_income'])
    annual_hike = (float(request.POST['annual_hike'])/100)
    current_annual_expenses = float(request.POST['current_annual_expenses'])
    current_total_savings = float(request.POST['current_total_savings'])
    percent_inv_high_return_assets = (float(request.POST['percent_inv_high_return_assets'])/100)

    percent_inv_low_return_assets = 1 - percent_inv_high_return_assets  # Percentage of savings in low return assets

    ##Assumptions
    sus_withdrawl_rate = 0.035  # sustainable withdrwal rate of 3.5%
    inflation = 0.07  # Inflation at 7%

    return_equity_inv = 0.14  # return from equity investments fixed at 14%
    return_fixed_inv = 0.07  # return on fixed income investments at 7%
    return_cash_inv = 0.04  # return from cash investments fixed at 4%

    # BaseCase
    return_high_inv_assets = return_equity_inv
    return_low_inv_assets = (return_fixed_inv + return_cash_inv) / 2

    ##Portfolio distribution

    # Balanced Case
    equity_comp_balanced = (100 - age) / 100  # Equity component = 100 -age in percentage
    fixed_comp_balanced = 1 - equity_comp_balanced  # Fixed Income component  = age in percentage

    # Relaxed Case
    equity_comp_relaxed = equity_comp_balanced - (0.5 * age / 100)  # Equity component  = Balanced  - 0.5 times age(%)
    fixed_comp_relaxed = 1 - equity_comp_relaxed

    # Aggressive case
    equity_comp_aggressive = equity_comp_balanced + (
                0.5 * age / 100)  # Equity component  = Balanced  + 0.5 times age(%)
    fixed_comp_aggressive = 1 - equity_comp_aggressive

    ##Calculated weighted return value on different investments

    # Base case -- calculates the weighted average return from high and low return assets
    return_base_case = (return_high_inv_assets * percent_inv_high_return_assets) + (
                return_low_inv_assets * percent_inv_low_return_assets)

    # Balanced case
    # calculates the weighted average return from allocation to equity and return from equity class and from fixed income and return in FI class and similarly for cash deposits
    # Assumes that FI is divided equally between FI and Cash
    return_balanced_case = (equity_comp_balanced * return_equity_inv) + 0.5 * (
                fixed_comp_balanced * return_fixed_inv) + 0.5 * (fixed_comp_balanced * return_cash_inv)

    # Relaxed case
    return_relaxed_case = (equity_comp_relaxed * return_equity_inv) + 0.5 * (
                fixed_comp_relaxed * return_fixed_inv) + 0.5 * (fixed_comp_relaxed * return_cash_inv)

    # Aggressive case
    return_aggressive_case = (equity_comp_aggressive * return_equity_inv) + 0.5 * (
                fixed_comp_aggressive * return_fixed_inv) + 0.5 * (fixed_comp_aggressive * return_cash_inv)

    # redefining variables
    # base case variables
    age_base = age
    current_annual_income_base = current_annual_income
    current_annual_expenses_base = current_annual_expenses
    current_total_savings_base = current_total_savings

    # relaxed case variables
    age_relaxed = age
    current_annual_income_relaxed = current_annual_income
    current_annual_expenses_relaxed = current_annual_expenses
    current_total_savings_relaxed = current_total_savings

    # balaced case variables
    age_balanced = age
    current_annual_income_balanced = current_annual_income
    current_annual_expenses_balanced = current_annual_expenses
    current_total_savings_balanced = current_total_savings

    # aggressive case variables
    age_aggressive = age
    current_annual_income_aggressive = current_annual_income
    current_annual_expenses_aggressive = current_annual_expenses
    current_total_savings_aggressive = current_total_savings

    # logic of calculations

    # Base case
    net_worth_base = current_total_savings_base  # initial net worth is equal to current savings
    savings_base = current_total_savings_base
    sus_withdrawl_base = sus_withdrawl_rate * net_worth_base

    while sus_withdrawl_base < current_annual_expenses_base:
        age_base += 1
        current_annual_income_base = current_annual_income_base * (1 + annual_hike)
        current_annual_expenses_base = current_annual_expenses_base * (1 + inflation)
        net_worth_base = (net_worth_base + (current_annual_income_base - current_annual_expenses_base)) * (
                    1 + return_base_case)
        total_savings_base = current_annual_income_base - current_annual_expenses_base + savings_base
        sus_withdrawl_base = net_worth_base * sus_withdrawl_rate

    # Balanced case
    net_worth_balanced = current_total_savings_balanced  # initial net worth is equal to current savings
    savings_balanced = current_total_savings_balanced
    sus_withdrawl_balanced = sus_withdrawl_rate * net_worth_balanced

    while sus_withdrawl_balanced < current_annual_expenses_balanced:
        age_balanced += 1
        current_annual_income_balanced = current_annual_income_balanced * (1 + annual_hike)
        current_annual_expenses_balanced = current_annual_expenses_balanced * (1 + inflation)
        net_worth_balanced = (net_worth_balanced + (
                    current_annual_income_balanced - current_annual_expenses_balanced)) * (1 + return_balanced_case)
        total_savings_balanced = current_annual_income_balanced - current_annual_expenses_balanced + savings_balanced
        sus_withdrawl_balanced = net_worth_balanced * sus_withdrawl_rate

    # Aggressive plan
    net_worth_aggressive = current_total_savings_aggressive  # initial net worth is equal to current savings
    savings_aggressive = current_total_savings_aggressive
    sus_withdrawl_aggressive = sus_withdrawl_rate * net_worth_aggressive

    while sus_withdrawl_aggressive < current_annual_expenses_aggressive:
        age_aggressive += 1
        current_annual_income_aggressive = current_annual_income_aggressive * (1 + annual_hike)
        current_annual_expenses_aggressive = current_annual_expenses_aggressive * (1 + inflation)
        net_worth_aggressive = (net_worth_aggressive + (
                    current_annual_income_aggressive - current_annual_expenses_aggressive)) * (
                                           1 + return_aggressive_case)
        total_savings_aggressive = current_annual_income_balanced - current_annual_expenses_balanced + savings_balanced
        sus_withdrawl_aggressive = net_worth_aggressive * sus_withdrawl_rate

    # relaxed plan
    net_worth_relaxed = current_total_savings_relaxed  # initial net worth is equal to current savings
    savings_relaxed = current_total_savings_relaxed
    sus_withdrawl_relaxed = sus_withdrawl_rate * net_worth_relaxed

    while sus_withdrawl_relaxed < current_annual_expenses_relaxed:
        age_relaxed += 1
        current_annual_income_relaxed = current_annual_income_relaxed * (1 + annual_hike)
        current_annual_expenses_relaxed = current_annual_expenses_relaxed * (1 + inflation)
        net_worth_relaxed = (net_worth_relaxed + (current_annual_income_relaxed - current_annual_expenses_relaxed)) * (
                    1 + return_relaxed_case)
        total_savings_relaxed = current_annual_income_relaxed - current_annual_expenses_relaxed + savings_relaxed
        sus_withdrawl_relaxed = net_worth_relaxed * sus_withdrawl_rate

    context= {
        'age_base': age_base,
        'net_worth_base': int(net_worth_base),
        'age_balanced': age_balanced,
        'net_worth_balanced': int(net_worth_balanced),
        'age_relaxed': age_relaxed,
        'net_worth_relaxed': int(net_worth_relaxed),
        'age_aggressive': age_aggressive,
        'net_worth_aggressive': int(net_worth_aggressive),
        'title': "FIRE Result"
    }

    return render(request, 'fijourney/fijourney_result.html', context)


