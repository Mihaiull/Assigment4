class MyVector:
    #Constructor
    def __init__(self, name_id, color, Type = 1, val = []):
        self.__name_id = name_id
        self.__color = color
        self.__Type = Type
        self.__val = val
    #End Of Constructor
    
    
    #Getters Setters
    def get_name_id(self):
        return self.__name_id
    def set_name_id(self, name_id):
        self.__name_id = name_id
    
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
    
    def get_type(self):
        return self.__Type
    def set_type(self, type):
        self.__Type = type
        
    def get_val(self):
        return self.__val
    def set_val(self, val):
        self.__val = val
    #End Of Getters Setters  
    
    
    #Operations:
    
    #Add two vectors
    #Overloading the + operator
    def __add__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot add vectors of different types")
        return MyVector(self.__name_id, self.__color, self.__Type, self.__val + other.__val)
    #Overloading the += operator
    def __iadd__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot add vectors of different types")
        self.__val += other.__val
        return self
    
    #Adding a scalar to MyVector:
    #Overloading the + operator(yet again sue me)
    #@Input: scalar
    def __radd__(self, scalar):
        return MyVector(self.__name_id, self.__color, self.__Type, self.__val + scalar)
    
    #Substract two vectors
    #Overloading the - operator
    def __sub__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot substract vectors of different types")
        return MyVector(self.__name_id, self.__color, self.__Type, self.__val - other.__val)
    #Overloading the -= operator
    def __isub__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot substract vectors of different types")
        self.__val -= other.__val
        return self
    
    #Multiply 2 vectors
    #Overloading the * operator
    def __mul__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot multiply vectors of different types")
        number = 0
        for i in range(len(self.__val)):
            number += self.__val[i] * other.__val[i]
        return number
    #Overloading the *= operator
    def __imul__(self, other):
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot multiply vectors of different types")
        number = 0
        for i in range(len(self.__val)):
            number += self.__val[i] * other.__val[i]
        return number
    
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
        if MyVector.get_type(self) != other.get_type():
            raise Exception("Cannot compare vectors of different types")
        return self.__val == other.__val
    
    
    #Output Methods   
    def __str__(self):
        return "Name: " + self.__name_id + ", Color: " + self.__color + ", Type: " + str(self.__Type) + ", Value: " + str(self.__val)
    
    def __repr__(self):
        return str(self)
    #End Of Output Methods