from menutitem import MenuItem

class Menu():
    def __init__(self, menuid, menuname, menutype, menudesc):
        self.menuid=menuid
        self.menuname=menuname
        self.menutype-menutype
        self.menudesc=menudesc

    def setMenu(self, i):
        self.menuitems.append(m)

    def getMenuItems(self):
        return self.menuitems

    def getMenuItemByID(self, id):
        reqMenuItem=None
        for m in self.menuitems:
            if m.menuitemid==id:
                reqMenuItem=m
                break
            return reqMenuItem