class Item:
    pay_rate = 0
    all = 0
    price = 0

    def __init__(self, name, one_pay, count):
        self.name = name
        self.one_pay = one_pay
        self.count = count
        Item.price = one_pay

    def calculate_total_price(self):
        total_price = self.one_pay * self.count
        return total_price

    def apply_discount(self):
        Item.price = self.one_pay * Item.pay_rate


