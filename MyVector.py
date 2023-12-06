from pickle import INT
from colorama import Fore, Style
import numpy as np

dictionary = {"r": "red", "g": "green", "b": "blue", "y": "yellow", "m": "magenta", "c": "cyan", "w": "white", "k": "black"}
#dictionary for coloring the output according to the color of the vector:
dictionary2 = {"r": "RED", "g": "GREEN", "b":"BLUE", "Y": "YELLOW", "m": "MAGENTA", "c": "CYAN", "w": "WHITE", "k": "BLACK"}
class MyVector:
    #Constructor
    def __init__(self, name_id, key, type = 1, val = []):
        self.__name_id = name_id
        self.__color = dictionary[key]
        self.__Type = type
        self.__val = val
        self.__key = key
    #End Of Constructor
    
    #Getters Setters
    
    def get_name_id(self):
        return self.__name_id
    def set_name_id(self, name_id):
        self.__name_id = name_id
    
    def get_color(self):
        return self.__color
    def set_color(self, key):
        self.__color = dictionary[key]
    
    def get_type(self):
        return self.__Type
    def set_type(self, type):
        self.__Type = type
        
    def get_val(self):
        return list(self.__val)
    def set_val(self, val):
        self.__val = val
        
    #For the sake of matplotlib not raising errors:
    def get_key(self):
        return self.__key
    
    #End Of Getters Setters  
    
    
    #Operations:
    
    #Add two vectors
    #Overloading the + operator
    
    #classic method
    #def __add__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot add vectors of different types")
        rez = []
        for i in range(len(self.__val)):
            rez.append(self.__val[i] + other.__val[i])
        return MyVector(self.__name_id, self.__key, self.__Type, rez)
    
    #numpy method
    def __add__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot add vectors of different types")
        list = [np.add(self.__val[i], other.val[i]) for i in range(len(self.__val))]
        return MyVector(self.__name_id, self.__key, self.__Type,)
    #Overloading the += operator
    
    #classic method
    #def __iadd__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot add vectors of different types")
        for i in range(len(self.__val)):
            self.__val[i] += other.__val[i]
        return self
    
    #numpy method
    def __iadd__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot add vectors of different types")
        self.__val = np.add(self.__val, other.__val)
        return self
    
    #Adding a scalar to MyVector:
    #Overloading the + operator(yet again sue me)
    
    #classic method
    #@Input: scalar
    #def __radd__(self, scalar):
        return MyVector(self.__name_id, self.__key, self.__Type, self.__val + scalar)
    
    #numpy method
    #@Input: scalar
    def __radd__(self, scalar):
        return MyVector(self.__name_id, self.__key, self.__Type, np.add(self.__val, scalar))
    
    #Substract two vectors
    #Overloading the - operator
    
    #classic method
    #def __sub__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot substract vectors of different types")
        return MyVector(self.__name_id, self.__key, self.__Type, [self.__val[i] - other.__val[i] for i in range(len(self.__val))])
    
    #numpy method
    def __sub__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot substract vectors of different types")
        return MyVector(self.__name_id, self.__key, self.__Type, np.subtract(self.__val, other.__val))
    
    #Overloading the -= operator
    
    #classic method
    #def __isub__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot substract vectors of different types")
        for i in range (len(self.__val)):
            self.__val[i] -= other.__val[i]
        return self
    
    #numpy method
    def __isub__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot substract vectors of different types")
        self.__val = np.subtract(self.__val, other.__val)
        return self
    
    #Multiply 2 vectors
    #Overloading the * operator
    
    #classic method
    #def __mul__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot multiply vectors of different types")
        number = 0
        for i in range(len(self.__val)):
            number += self.__val[i] * other.__val[i]
        return number
    
    #numpy method
    def __mul__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot multiply vectors of different types")
        multi = np.multiply(self.__val, other.__val)
        suma = 0
        for i in range(len(self.__val)):
            suma += self.__val[i]
        return multi
    
    
    #Overloading the *= operator
    
    #classic method
    #def __imul__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot multiply vectors of different types")
        number = 0
        for i in range(len(self.__val)):
            number += self.__val[i] * other.__val[i]
        return number
    
    #numpy method
    def __imul__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot multiply vectors of different types")
        multi = np.multiply(self.__val, other.__val)
        self.__val = list(multi)
        suma = 0
        for i in range(len(self.__val)):
            suma += self.__val[i]
        return suma
    
    #Sum of elements in a vector:
    def sum(self):
        number = 0
        for i in range(len(self.__val)):
            number += self.__val[i]
        return number
    
    #Product of elements in a vector:
    def prod(self):
        number = 1
        for i in range(len(self.__val)):
            number *= self.__val[i]
        return number
    
    #Average of elements in a vector:
    def avg(self):
        number = 0
        for i in range(len(self.__val)):
            number += self.__val[i]
        return number / len(self.__val)
    
    #Minimum of elements in a vector:
    def min(self):
        number = self.__val[0]
        for i in range(1,len(self.__val)):
            if number > self.__val[i]:
                number = self.__val[i]
        return number
    
    #Maximum of elements in a vector:
    def max(self):
        number = self.__val[0]
        for i in range(1,len(self.__val)):
            if number < self.__val[i]:
                number = self.__val[i]
        return number
    #End Of Operations
    
    def __eq__(self, other):
        #if MyVector.get_type(self) != other.get_type(self):
            #raise Exception("Cannot compare vectors of different types")
        if type(other) == int:
            return self.get_val() == other
        elif type(other) == MyVector:
            return self.get_val() == other.get_val()
    
    
    #Output Methods   
    def __str__(self):
        return "Name: " + Fore.LIGHTCYAN_EX + self.__name_id + Style.RESET_ALL + ", Color: "+ self.__color + ", Type: " + Fore.BLUE + str(self.__Type) + Style.RESET_ALL + ", Value: " + Fore.LIGHTMAGENTA_EX + str(self.__val) + Style.RESET_ALL
    
    
    def __repr__(self):
        return str(self)
    #End Of Output Methods