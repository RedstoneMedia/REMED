import math,random,time

class Rechnen:

    selflist = []

    def __init__(self,List,punktvorstrich=1):
        self.string = List
        self.punktvorstrich = punktvorstrich
        self.selflist.append(self)
