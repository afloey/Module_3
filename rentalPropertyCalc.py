

class rentalCalc():


    def __init__(self):
        return None
    

    def income(self):
        self.rental_inc = int(input("What is your rental income?  "))
        self. laundry_inc = int(input("What is your laundry income?  "))
        self. misc_inc = int(input("What is your misc income? "))
        print("Your income is ${income}.")
        return sum((self.rental_inc, self.laundry_inc, self.misc_inc) * 12)

    def expenses(self):
        self.taxes_exp = int(input("What are you paying in taxes?  "))
        self.util_exp = int(input("What are your utility expenses?  "))
        self.vac_exp = int(input("What are your vacancy expenses?  "))
        print("Your expenses add up to ${expenses}.")
        return sum((self.taxes_exp, self.util_exp, self.vac_exp) * 12)

    def cashFlow(self):
        print("Your cash flow is ${cashFlow}")
        return ((self.income() - self.expenses()) * 12)

    def cashReturn(self):
        self. down_pay_ret = int(input("What is your down payment:  "))
        self.close_ret = int(input("What is your closing cost?  "))
        print("Your Cash Return is ${cashReturn}.")
        return sum(self.down_pay_ret, self.close_ret)

    def annual_ROI(self):
        print ("Your annual ROI is ${annual_ROI}.")
        return ((rentalCalc.cashFlow() / rentalCalc.cashReturn()) * 100)


rental1 = rentalCalc()

rental1.income()
rental1.expenses()
rental1.cashFlow()
rental1.cashReturn()
rental1.annual_ROI()
