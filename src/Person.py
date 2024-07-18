from random import randint

class Person:

    def __init__(self,id=randint(1,999),name="User",height=0,weight=[]):
        self._id = id
        self._name = name
        self._height = height
        self._weight = weight
        
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,setname):
        if not isinstance(setname,str):
            raise TypeError("Name must be string type")
        self._name = setname
        print(" NAME SAVED ".center(20,'='))

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,setheight):
        if not isinstance(setheight,float):
            raise TypeError("Must be decimal height in inches")
        self._height = setheight
        print(" HEIGHT SAVED ".center(20,'='))

    def weight(self):
        return self._weight
    
    def addWeight(self,weight):
        self._weight.append(weight)