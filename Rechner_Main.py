import math,random,time

class Rechnen:

    selflist = []

    def __init__(self,List,punktvorstrich=1):
        self.List = List
        self.ergebnis = 0
        self.punktvorstrich = punktvorstrich
        self.selflist.append(self)
