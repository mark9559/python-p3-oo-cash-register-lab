#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount) // 100
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.items.pop()
            self.total -= last_item_price

    def reset_register_totals(self):
        self.total = 0
        self.items = []

    def test_void_last_transaction_with_multiples(self):
        self.cash_register.add_item("tomato", 1.76, 2)
        self.cash_register.void_last_transaction() 
        assert(self.cash_register.total == 1.76)
        self.cash_register.void_last_transaction()
        assert(self.cash_register.total == 0.0)
