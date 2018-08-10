class Zaehler(object): 
    Anzahl = 0 
 
    def __init__(self): 
        type(self).Anzahl += 1
    def __del__(self): 
        type(self).Anzahl -= 1


class Bierglas(Zaehler):
    def __init__(self, sorte, fuellstand):
        self.Sorte = sorte
        self.__fuellstand = fuellstand
        Zaehler.__init__(self)

    def fuellen(self):
        self.__fuellstand = 500
    def schluck_nehmen(self):
        if self.__fuellstand > 0:
            if self.__fuellstand < 50:
                self.__fuellstand = 0
            else:
                self.__fuellstand -= 50
    def verbleibend(self):
        print("Es sind noch " + str(self.__fuellstand) + " ml Bier im Glas")
        return self.__fuellstand
    
bier = Bierglas("Weizen", 0)
print(bier.verbleibend())
print(bier.Anzahl)
bier.fuellen()
bier.schluck_nehmen()
print(bier.verbleibend())
print(bier.Anzahl)