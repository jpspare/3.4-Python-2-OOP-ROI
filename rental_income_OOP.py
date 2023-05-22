class RentalIncomeROI():
    """
        The RentalIncomeROI takes input of multiple values and uses them to calculate the
        cash on cash ROI for a rental property.
    """

    # Initializes the global variables
    def __init__(self):
        self.total_monthly_income = 0
        self.total_monthly_expenses = 0
        self.monthly_cash_flow = 0
        self.total_investment = 0


    # income method calculates the total monthly income
    def income(self):
        print('Please enter the amount of income you make on the following sources. Please enter a number only, no punctuation.')
        income_sources = {}

        # User input for all the income
        income_sources['Rental Income'] = input('Rental Income: ')
        income_sources['Laundry Income'] = input('Laundry Income: ')
        income_sources['Storage Income'] = input('Storage Income: ')
        income_sources['Miscellany Income'] = input('Miscellany Income: ')
        
        # Attempt to convert user input to integers, with one loop to retry if number is not an integer
        try:
            for key, value in income_sources.items():
                try:
                    income_sources[key] = int(value)
                except ValueError:
                    print("Please enter the income as an integer with no punctuation")
                    income_sources[key] = int(input(f'{key}: '))
        except ValueError:
            print('\nPlease try again - this time make sure all numbers are integers only, no punctuation, please!')
            return self.income()

        # Calculate total monthly income and print
        self.total_monthly_income = sum(income_sources.values())
        print(f'\nTotal Monthly Income is: ${self.total_monthly_income}')              

    # expenses method calculates total monthly expenses based on user input
    def expenses(self):
        print('\nPlease enter the expenses for each of the following items - make sure to enter a number only, no punctuation.')
        rental_expenses = {}

        #User input for all the expenses
        rental_expenses['Taxes'] = input('Monthly Taxes: ')
        rental_expenses['Insurance'] = input('Monthly Insurance: ')
        rental_expenses['Utilities'] = input('Do you pay for any utilties? Yes/No: ')
        if rental_expenses['Utilities'].lower() == 'no':
            rental_expenses['Utilities'] = 0
        else:
            try:
                print('Please enter a number with no punctuation for the following utilties:')
                electricity = int(input('Electricity: '))
                water = int(input('Water: '))
                sewer = int(input('Sewer: '))
                garbage = int(input('Garbage: '))
                gas = int(input('Gas: '))
            except ValueError:
                print('\nPlease try again - this time make sure all numbers are integers only, no punctuation, please!')
                return self.expenses()
            rental_expenses['Utilities'] = sum([electricity, water, sewer, garbage, gas])
        rental_expenses['HOA'] = input('Monthly HOA: ')
        rental_expenses['Lawn/Snow Removal'] = input('Lawn/Snow Removal: ')
        rental_expenses['Vacancy'] = input('Vacancy: ')
        rental_expenses['Repairs'] = input('Repairs: ')
        rental_expenses['CapEx Savings'] = input('Monthly CapEx Savings: ')
        rental_expenses['Property Management'] = input('Property Management: ')
        rental_expenses['Mortgage'] = input('Monthly Mortgage: ')

        # Attempt to convert user input to integers, with one loop to retry if number is not an integer
        try:
            for key, value in rental_expenses.items():
                try:
                    rental_expenses[key] = int(value)
                except ValueError:
                    print("Please enter the expense as an integer with no punctuation")
                    rental_expenses[key] = int(input(f'{key}: '))
        except ValueError:
            print('\nPlease try again - this time make sure all numbers are integers only, no punctuation, please!')
            return self.expenses()
        
        # Calculate total monthly expenses and print
        self.total_monthly_expenses = sum(rental_expenses.values())
        print(f'\nTotal Monthly Expenses are: ${self.total_monthly_expenses}')

    # cash_flow method caculates and prints the montly cash flow based on monthly income and expenses
    def cash_flow(self):
        self.monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
        print(f'\nTotal Monthly Cash Flow is: ${self.monthly_cash_flow}')

    # roi method takes input on total investment and returns 1. the annual cash flow, 2. the ROI, and 3. the Cash-on-Cash ROI
    def roi(self):
        print('\nPlease enter an amount for the following investments in the property - make sure to enter a number only, no punctuation.')
        rental_investment = {}

        #User input for all the expenses
        rental_investment['Down Payment'] = input('Down Payment: ')
        rental_investment['Closing Costs'] = input('Closing Costs: ')
        rental_investment['Rehab Budget'] = input('Rehab Budget: ')
        rental_investment['Misc Other'] = input('Misc Other: ')

        # Attempt to convert user input to integers, with one loop to retry if number is not an integer
        try:
            for key, value in rental_investment.items():
                try:
                    rental_investment[key] = int(value)
                except ValueError:
                    print("Please enter the investment as an integer with no punctuation")
                    rental_investment[key] = int(input(f'{key}: '))
        except ValueError:
            print('\nPlease try again - this time make sure all numbers are integers only, no punctuation, please!')
            return self.roi()
        
        # Calculate total investment and print
        self.total_investment = sum(rental_investment.values())
        print(f'\nTotal Investment: ${self.total_investment}')

        # Calculate and print Annual Cash Flow, ROI (%), and Cash on Cash ROI
        annual_cash_flow = self.monthly_cash_flow * 12
        roi_percentage = (annual_cash_flow / self.total_investment) * 100

        print(f'\nBased on your input of ${self.total_monthly_income} for monthly income, ${self.total_monthly_expenses} for monthly expenses, and ${self.total_investment} as your total investment:')
        print(f'- Annual Cash Flow: ${annual_cash_flow}\n- Cash-on-Cash ROI: {roi_percentage}%')



example = RentalIncomeROI()
example.income()
example.expenses()
example.cash_flow()
example.roi()
