# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:03:47 2017

@author: mark
"""

class CustomMetaclass(type):    
    def __init__(cls, name, bases, dct):        
        print("Creating class {} using CustomMetaclass".format(name))        
        super().__init__(name, bases, dct)
 
class BaseClass(object, metaclass=CustomMetaclass):    
    pass
 
class Subclass1(BaseClass):    
    pass 