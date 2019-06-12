from menuitem import MenuItem

class OrderItem():
    def __init__(self, menuitem, quantity):
        self.menuitem=menuitem
        self.quantity=quantity

    def getMenuItem(self):
        return self.menuitem

    def getQuantity(self):
        return self.quantity
        