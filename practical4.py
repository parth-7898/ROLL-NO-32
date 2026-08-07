from datetime import datetime
import random

class PaymentStrategy:
    def pay(self, customer, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, customer, amount):
        print(f"Payment Method : Credit Card")
        print(f"Customer       : {customer}")
        print(f"Amount         : ₹{amount}")


class PayPalPayment(PaymentStrategy):
    def pay(self, customer, amount):
        print(f"Payment Method : PayPal")
        print(f"Customer       : {customer}")
        print(f"Amount         : ₹{amount}")


class UPIPayment(PaymentStrategy):
    def pay(self, customer, amount):
        print(f"Payment Method : UPI")
        print(f"Customer       : {customer}")
        print(f"Amount         : ₹{amount}")

class CashPayment(PaymentStrategy):
    def pay(self, customer, amount):
        print(f"Payment Method : Cash")
        print(f"Customer       : {customer}")
        print(f"Amount         : ₹{amount}")


class PaymentContext:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, customer, amount):

        if amount <= 0:
            print("\nInvalid Amount! Payment Failed.")
            return
            

        transaction_id = "TXN" + str(random.randint(10000, 99999))

        now = datetime.now()

        print("\n" + "=" * 50)
        print("         PAYMENT RECEIPT")
        print("=" * 50)

        self.strategy.pay(customer, amount)

        print(f"Transaction ID : {transaction_id}")
        print(f"Date           : {now.strftime('%d-%m-%Y')}")
        print(f"Time           : {now.strftime('%I:%M:%S %p')}")
        print("Status         : Payment Successful")

        print("=" * 50)
        print("Thank You for Your Payment!")
        print("=" * 50)


customer = input("Enter Customer Name: ")
amount = float(input("Enter Amount: ₹"))

print("\nSelect Payment Method")
print("1. Credit Card")
print("2. PayPal")
print("3. UPI")
print("4. Cash")

choice = int(input("Enter Choice: "))

if choice == 1:
    strategy = CreditCardPayment()

elif choice == 2:
    strategy = PayPalPayment()

elif choice == 3:
    strategy = UPIPayment()

elif choice == 4:
    strategy = CashPayment()

else:
    print("Invalid Choice!")
    exit()

payment = PaymentContext(strategy)
payment.pay(customer, amount)