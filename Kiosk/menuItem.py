class MenuItem():
    def __init__(self, itemid, itemname, itemprice, itemtype, itemdesc):
        self.itemid=itemid
        self.itemname=itemname
        self.itemprice=itemprice
        self.itemtype=itemtype
        self.itemdesc=itemdesc
        
    def getItemID(self):
        return self.itemid

    def getItemName(self):
        return self.itemname

    def getItemPrice(self):
        return self.itemprice

    def getItemDesc(self):
        return self.itemdesc

    def __str__(self):
        return self.itemname