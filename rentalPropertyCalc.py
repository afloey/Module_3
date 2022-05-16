


from tkinter.tix import INTEGER


class rentalCalc():
   def __init__(self, rental_inc, laundry_inc, storage_inc, misc_inc, taxes_exp, util_exp, vac_exp, down_pay_ret, close_ret):
        self.rental_inc = rental_inc
        self.laundry_inc = laundry_inc
        self.storage_inc = storage_inc
        self.misc_inc = misc_inc
        self.taxes_exp = taxes_exp
        self.util_exp = util_exp
        self.vac_exp = vac_exp
        self.down_pay_ret= down_pay_ret
        self.close_ret = close_ret
    
        def income():
            (sum(self.rental_inc, self.laundry_inc, self.storage_inc, self.misc_inc)) * 12
        
        def expenses():
            (sum(self.taxes_exp, self.util_exp, self.vac_exp)) * 12

        def cashFlow():
            (self.income() - self.expenses()) * 12

        def cashReturn():
            sum(self.down_pay_ret, self.close_ret)

        def annual_ROI():
            cashFlow / cashReturn * 100


rentalIncome= rentalCalc()
response = input("Welcome to the Rental Income Calculator! Type anything to begin: ")

def run():

    while True:

        print("Income- rental income: ")
        if response == INTEGER:
            rentalIncome.rental_inc()
        
        print("Income- laundry income: ")
        if response == INTEGER:
            rentalIncome.laundry_inc()

        print("Income- storage income: ")
        if response == INTEGER:
            rentalIncome.storage_inc()
        
        print("Income- misc income: ")
        if response == INTEGER:
            rentalIncome.misc_inc()

        print("Expenses- Taxes: ")
        if response == INTEGER:
            rentalIncome.taxes_exp()
        
        print("Expenses- utilities: ")
        if response == INTEGER:
            rentalIncome.util_exp()
        
        print("Expenses- vacancy: ")
        if response == INTEGER:
            rentalIncome.vac_exp()

        print("Down Payment: ")
        if response == INTEGER:
            rentalIncome.down_pay_ret()

        print("Closing costs: ")
        if response == INTEGER:
            rentalIncome.close_ret()

        print("Your annual cash flow is: {cashFlow}")
        print("Your annual Cash on Cash ROI is {annual_ROI}")
    
    else:
        print("Please type a number.")

run()


