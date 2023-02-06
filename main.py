property_tax_rate = 0.01
insurance_rate = 200
term = 30
property_price = 1400000
rent_amount = 3700
mortgage_interest = 0.05
inflation_rate = 0.067
tax_rate = 0.25
tax_deduction_rate = 0.0
property_inflation_rate = 0.03
rent_inflation = 0.02


def mortgage_amortization(principal, interest_rate, property_tax_rate, insurance_rate, term, inflation_rate):
    monthly_interest_rate = interest_rate / 12
    monthly_payment = principal * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-term * 12)))
    property_tax_payment = principal * property_tax_rate / 12
    insurance_payment = insurance_rate
    total_monthly_payment = monthly_payment + property_tax_payment + insurance_payment

    print("Monthly Payment: ${:.2f}".format(monthly_payment))
    print("Property Tax Payment: ${:.2f}".format(property_tax_payment))
    print("Insurance Payment: ${:.2f}".format(insurance_payment))
    print("Total Monthly Payment: ${:.2f}".format(total_monthly_payment))

    payments = []
    total_payout = 0
    for i in range(term * 12):
        interest_paid = principal * monthly_interest_rate
        principal_paid = monthly_payment - interest_paid
        principal = principal - principal_paid
        payments.append({"period": i + 1, "interest_paid": interest_paid, "principal_paid": principal_paid,
                         "remaining_balance": principal})

        total_payout = total_payout + monthly_payment

    print("Total net payout: ${:.2f}".format(total_payout))
    current_value_of_future_payout = total_payout * (1 - inflation_rate) ** term
    print("Current value of future payout: ${:.2f}".format(current_value_of_future_payout))
    return payments


payments = mortgage_amortization(property_price, mortgage_interest, property_tax_rate, insurance_rate, term,
                                 inflation_rate)

print("Amortization Schedule:")
for payment in payments:
    print("Period: {:<7} Interest Paid: ${:<7.2f} Principal Paid: ${:<7.2f} Remaining Balance: ${:<7.2f}".format(
        payment["period"], payment["interest_paid"], payment["principal_paid"], payment["remaining_balance"]))





def calculate_annual_rent(rent, increase_rate, years):
    annual_rents = []
    for year in range(years):
        rent *= (1 + increase_rate)
        annual_rents.append(rent)
    return annual_rents

def calculate_total_rent(annual_rents):
    total_rent = 0
    for annual_rent in annual_rents:
        total_rent += annual_rent * 12
    return total_rent


def calculate_total_cost_to_buy(property_price, down_payment, mortgage_interest, term, tax_deduction_rate):
    loan_amount = property_price - down_payment
    monthly_interest_rate = mortgage_interest / 12
    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-term * 12)))
    interest_paid = (monthly_payment * term * 12 - loan_amount) * tax_deduction_rate
    total_cost = monthly_payment * term * 12 + down_payment - interest_paid
    return total_cost

def minimum_down_payment(property_price, rent_amount, mortgage_interest, term, inflation_rate,
                         tax_deduction_rate, property_inflation_rate, rent_inflation):

    down_payment = 0
    annual_rents = calculate_annual_rent(rent_amount, rent_inflation, term)
    total_cost_to_rent = calculate_total_rent(annual_rents)
    appreciated_property_value = property_price * (1 + inflation_rate - mortgage_interest) ** term
    appreciation = appreciated_property_value - property_price
    while True:
        total_cost_to_buy = calculate_total_cost_to_buy(property_price, down_payment, mortgage_interest, term,
                                                        tax_deduction_rate)
        if (total_cost_to_buy - appreciation) < total_cost_to_rent or down_payment >= property_price:
            print("Minimum down payment required to make it better to buy: ${:.2f}".format(down_payment))
            break
        down_payment += 1000

    appreciated_property_value = property_price * (1 + property_inflation_rate) ** term
    print("Appreciated property value: ${:.2f}".format(appreciated_property_value))


minimum_down_payment(property_price, rent_amount, mortgage_interest, term, inflation_rate, tax_deduction_rate,
                     property_inflation_rate, rent_inflation)
