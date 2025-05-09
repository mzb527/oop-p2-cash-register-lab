#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        if not isinstance(discount, int) or not (0 <= discount <= 100):
            print("Not valid discount, setting to 0.")
            discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity):
        if not isinstance(price, (int, float)) or price <= 0:
            print("Invalid price, must be a positive number.")
            return
        if not isinstance(quantity, int) or quantity <= 0:
            print("Invalid quantity, must be a positive integer.")
            return
        self.total += price * quantity
        self.items.append((item, quantity))
        self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})

    def apply_discount(self):
        if self.discount == 0:
            print("No discount available.")
            return
        if self.total == 0:
            print("Cannot apply discount to an empty register.")
            return
        self.total *= (1 - self.discount / 100)
        print(f"Discount applied. New total: {self.total:.2f}")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No previous transactions to void.")
            return
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        if (last_transaction["item"], last_transaction["quantity"]) in self.items:
            self.items.remove((last_transaction["item"], last_transaction["quantity"]))
        print(f"Last transaction voided. New total: {self.total:.2f}")

# Example Usage
register = CashRegister(20)
register.add_item("Apple", 2, 5)
register.apply_discount()
register.void_last_transaction()
print(register.total)
class CashRegister:
  pass
