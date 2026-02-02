class Payments:
    def payamount(self,amount):
        print(f"Paying Amount: {amount}")
        print(f"Payment Successfull: {amount}")


class UPI(Payments):
    def pay(self,amount):
        print(f"Paying Through UPI")
        super().payamount(amount)

class CreditCard(Payments):
    def pay(self,amount):
        print(f"Paying Through Credit Card")
        super().payamount(amount)

upi_pay = UPI()
credit_pay = CreditCard()
upi_pay.pay(1000)
credit_pay.pay(500)
