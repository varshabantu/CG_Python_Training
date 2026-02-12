import logging

logging.basicConfig(
    filename="order.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class Order:

    tax_percentage = 10

    def __init__(self, oid, price, qty):
        self.oid = oid
        self.price = price
        self.qty = qty
        self.placed = False
    # object method
    def place_order(self):
        self.placed = True
        logging.info("Order placed : %s", self.oid)

    # object method
    def cancel_order(self):
        logging.info("Order cancelled : %s", self.oid)

    # object method
    def calculate_total_price(self):
        if not self.placed:
            logging.error("Order not placed : %s", self.oid)
            return
        total = self.price * self.qty
        total += total * Order.tax_percentage / 100
        logging.info("Total price for %s : %s", self.oid, total)
        return total

    # class method
    @classmethod
    def update_tax_percentage(cls, tax):
        cls.tax_percentage = tax
        logging.info("Tax updated to %s", tax)

o = Order(1, 500, 2)
o.place_order()
o.calculate_total_price()
Order.update_tax_percentage(10)
o.calculate_total_price()
o.cancel_order()