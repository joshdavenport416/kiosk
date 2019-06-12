from menuItem import MenutItem
from ordertiems import OrderItem
from payment import payment

class Order():
    def __init__(self):
        self.orderitems=[]

    def addOrderItems(self, orderitem):
        self.orderitems.append(orderitem)

    def getOrderItems(self):
        return self.orderitems

    def calcTotal(self):
        total=0.0
        for o in self.orderitems:
            total += o.itemprice * o.quantity
        payment=Payment(total)
        return payment