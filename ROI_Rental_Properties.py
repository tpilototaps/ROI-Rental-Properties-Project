import time

class Bigger_pockets():
    def __init__(self, total_income = 0, total_expenses = 0, monthly_cash_flow = 0, annual_cash_flow = 0, cash_on_cash_roi = 0, total_investment = 0):
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.monthly_cash_flow = monthly_cash_flow
        self.annual_cash_flow = annual_cash_flow
        self.cash_on_cash_roi = cash_on_cash_roi
        self.total_investment = total_investment

    def income(self):
        rental_income = input("RENTAL INCOME?: ")
        laundry = input("LAUNDRY INCOME?: ")
        storage = input("STORAGE INCOME?: ")
        misc = input("MISCELLANEOUS INCOME?: ")
        self.total_income = int(rental_income) + int(laundry) + int(storage) + int(misc)
        print(f'\nYOUR TOTAL INCOME IS {self.total_income}\n')

    def expenses(self):
        tax = input("TAX PAID: ")
        insurance = input("INSURANCE PAID: ")
        while True:
            utilities_paid = input("ANY UTILITIES PAID BY YOU? ENTER Y OR N ")
            if utilities_paid == 'Y'.lower():
                electric = input("ELECTRIC PAID: ")
                water = input("WATER PAID: ")
                sewer = input("SEWER PAID: ")
                garbage = input("GARBAGE PAID: ")
                gas = input("GAS PAID: ")
                self.total_expenses = int(electric) + int(water) + int(sewer) + int(garbage) + int(gas)
                break
            elif utilities_paid == 'N'.lower():
                break
            elif utilities_paid != 'Y' or 'N':
                print("THAT IS NOT A VALID INPUT, PLEASE TRY AGAIN")
                time. sleep(3)
        hoa = input("HOA FEES: ")
        lawn_snow = input("LAWN OR SNOW PAID: ")
        vacancy = input("VACANY PROVISIONS PAID: ")
        repairs = input("REPAIRS PAID: ")
        capEx = input("CAPEX PAID: ")
        prop_management = input("PROPERTY MANAGEMENT PAID: ")
        mortage = input("MORTAGE PAID: ")
        self.total_expenses = int(self.total_expenses) + int(tax) + int(insurance) + int(hoa) + int(lawn_snow) + int(vacancy) + int(repairs) + int(capEx) + int(prop_management) + int(mortage)
        print(f"\nYOUR TOTAL EXPENDITURE IS ${self.total_expenses}\n")

    def cash_flow(self):
        self.monthly_cash_flow = self.total_income - self.total_expenses
        self.annual_cash_flow = self.monthly_cash_flow * 12

    def roi(self):
        down_payment = input("DOWN PAYMENT PAID: ")
        closing_costs = input("CLOSING COST: ")
        rehab_budget = input("REHAB BUDGET: ")
        misc_other = input("OTHER MISCELLANEOUS COSTS: ")
        self.total_investment = int(down_payment)+ int(closing_costs) + int(rehab_budget) + int(misc_other)
        return_of_investment = self.annual_cash_flow/self.total_investment * 100
        return return_of_investment

test = Bigger_pockets()

test.income()
time.sleep(3)
test.expenses()
time.sleep(3)
test.cash_flow()
print(f'\nYOUR RETURN ON INVESTMENT (ROI) IS {test.roi()}%\n')
time.sleep(3)
print('\nTHANK YOU FOR USING OUR ROI CALCULATOR!\n')



