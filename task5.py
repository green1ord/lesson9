class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Р—Р°РїСѓСЃРє РѕС‚СЂРёСЃРѕРІРєРё')


class Pen(Stationery):
    def draw(self):
        print('Р СѓС‡РєР° СЂРёСЃСѓРµС‚')


class Pencil(Stationery):
    def draw(self):
        print('РљР°СЂР°РЅРґР°С€ СЂРёСЃСѓРµС‚')


class Handle(Stationery):
    def draw(self):
        print('РњР°СЂРєРµСЂ СЂРёСЃСѓРµС‚')


pen = Pen('СЂСѓС‡РєР°')
pencil = Pencil('РєР°СЂР°РЅРґР°С€')
handle = Handle('РјР°СЂРєРµСЂ')

pen.draw()
pencil.draw()
handle.draw()