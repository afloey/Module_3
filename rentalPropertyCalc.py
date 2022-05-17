


class rentalCalc():
   def __init__(self):
       self.rental_inc
       self.laundry_inc
       self.misc_inc
       self.taxes_exp
       self.util_exp
       self.vac_exp
       self.down_pay_ret
       self.close_ret

    
    def income(self):
        self.rental_inc = input(int("What is your rental income?  "))
        self.laundry_inc = input(int("What is your laundry income?  "))
        self.misc_inc = input(int("What is your misc income? "))
        print("Your income is ${sum(self.rental_inc, self.laundry_inc, self.misc_inc) * 12)}.")

    def expenses(self):
        self.taxes_exp = input(int("What are you paying in taxes?  "))
        self.util_exp = input(int("What are your utility expenses?  "))
        self.vac_exp = input(int("What are your vacancy expenses?  "))
        return sum(self.taxes_exp, self.util_exp, self.vac_exp) * 12
        print("Your expenses add up to ${expenses}.")

    def cashFlow(self):
        return (self.income() - self.expenses()) * 12
        print("Your cash flow is ${cashFlow}")

    def cashReturn(self):
        self. down_pay_ret = input(int("What is your down payemnt:  "))
        self.close_ret = input(int("What is your closing cost?  "))
        return sum(self.down_pay_ret, self.close_ret)
        print("Your Cash Return is ${cashReturn}.")

    def annual_ROI(self):
        return (rentalCalc.cashFlow() / rentalCalc.cashReturn()) * 100
        print("Your annual ROI is ${annual_ROI}.")

rentalCalc.income()
rentalCalc.expenses()
rentalCalc.cashFlow()
rentalCalc.cashReturn()
rentalCalc.annual_ROI()
