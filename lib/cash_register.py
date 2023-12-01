#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_item = {"title": "", "price": 0, "quantity": 1}

  def add_item(self, title, price, quantity=1):
    self.last_item["title"] = title
    self.last_item["price"] = price
    self.last_item["quantity"] = quantity
    i = quantity
    while i >= 1:
      self.items.append(title)
      i -= 1

    total_price = price * quantity
    self.total = self.total + total_price 

  def apply_discount(self):
    if self.discount != 0:
      self.total = self.total - (self.discount * 0.01 * self.total)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total = self.total - (self.last_item["price"] * self.last_item["quantity"])