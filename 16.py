#!/usr/bin/python
# -*- coding: utf-8 -*-

class SampleClass:
    def __init__(self):
        print("Constructor")
        self.nm = "SampleClass"
    
    def printName(self):
        print(self.nm)

obj = SampleClass()

obj.printName()
print(obj.nm)   # to output the attribute alone


class Parent:               # parent class
    def print_name(self):
        print("parent class")
        
class Child(Parent):        # inheritance of parent class
    def print_child(self):
        print("child class")
        
obj = Child()
obj.print_name()
obj.print_child()


class Parent:               # parent class
    def print_name(self):
        print("parent class")
        
class Child(Parent):        # inheritance of parent class
    def print_child(self):
        print("child class")
        
    def print_name(self):
        print("child class")
        Parent.print_name()
                
obj = Child()
obj.print_name()


class IterClass:
    def __init__(self, x):
        self.massiv = x
        self.ind = 0    # index
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.ind >= len(self.massiv):
            self.ind = 0        # set the index to zero
            raise StopIteration # generate exception
        else:
            item = self.massiv[self.ind]
            self.inf += 1
            return item

obj = IterClass([1, 2, 3])
for i in obj:
    print(i, end = " ") # will output 1 2 3


class StaticSample:
    @staticmethod
    def ssum(x, y):
        return (x + y)
    
    def msum(self, x, y):
        return (x + y)
    
print(StaticSample.ssum(2, 2))  # call before definition of the object

obj = StaticSample()
print(obj.msum(2, 2))   # call of a regular method
print(obj.ssum(2, 2))   # call of a static method through an object


class Sample:
    def func(self, x, y):
        raise NotImplementedError("not implemented")
        
    def msum(self, x, y):
        return (x + y)


from abc import *

class Sample:
    @abstracmethod
    def func(self, x, y):
        pass
    
    def msum(self, x, y):
        return (x + y)


class ReloadClass:
    def __init__(self):
        slef.x = 0
        self.a = [1, 2, 3]
    
    def __eq__(self, x):
        return self.x == y
    
    def __contains__(self, y):
        return y in self.a
    
o = ReloadClass()

if o == 10:
    print("true")
else:
    print("false")  # will output false

if 3 in o:
    print("true")   # will output true
else:
    print("false")
    
    
class MyClass:
    def __init__(self, x):
        self.__Property1 = x
        
    def set_property(self, x):
        self.__Property1 = x
        
    def get_property(self):
        return self.__Property1
    
o = MyClass(5)          # __Property1 = 5
print(o.get_property()) # will output 10
o.set_property(10)      # __Property1 = 10

try:
    print(o.__Property1)        # will result in an error
except AttributeError as msg:
    print(msg)                  # will output message for an error
    
o.__MyClass__Property1 = 20     # no error, __Property1 = 20
print(o.get_property())         # will output 20


class PropertySampleClass:
    def __init__(slef, x):
        self.__p = x
        
    def get_p(self):
        return self.__p
    
    def set_p(self, x):
        self.__p = x
        
    def del_p(self):
        del self.__p
        
    prop = property(get_p, set_p, del_p, "Info")
        
o = PropertySampleClass(1)
print(o.prop)   # calls method get_p
o.prop = 5      # calls method set_P
del o.prop      # calls method del_p


def deco(d):
    print("this is decorator")
    return d

@deco
class SampleClass:
    def __init__(self, value):
        slef.v = value
        
o = SampleClass(1)
print(o.v)
