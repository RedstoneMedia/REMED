import random
import time


class Rechnen:

    selflist = []

    def __init__(self, List, punktvorstrich=1):
        self.List = List
        self.ergebnis = 0
        self.punktvorstrich = punktvorstrich
        self.selflist.append(self)
        self.Aus_Rechnen()

    # hier bist du Rcihtig
    def Aus_Rechnen(self):
        while not self.only1(self.List) == True:
            del self.List[-1]
            print(self.List)

    @staticmethod
    def only1(l):
        true_found = False
        for v in l:
            if v:
                # a True was found!
                if true_found:
                    # found too many True's
                    return False
                else:
                    # found the first True
                    true_found = True
        # found zero or one True value
        return true_found




