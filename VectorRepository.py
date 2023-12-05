from MyVector import MyVector
from matplotlib import pyplot as plt

class VectorRepository:
    def __init__(self):
        self.__vectors = []
        
    def add_vector(self, vector):
        if not isinstance(vector, MyVector):
            raise Exception("Not a vector")
        if vector.get_name_id() == "":
            raise ValueError("Invalid name_id")
        if vector.get_name_id() in [x.get_name_id() for x in self.__vectors]:
            raise ValueError("There already exists a vector with the given name_id")
        self.__vectors.append(vector)
        
    def get_vectors(self):
        return self.__vectors if len(self.__vectors) > 0 else "No vectors"
    
    #get vector at a given index:
    def get_vector(self, index):
        return self.__vectors[index]
    
    #update a vector at a given index:
    def update_vector(self, index, new_vector):
        self.__vectors[index] = new_vector
        
    #update a vector identified by name_id:
    def update_vector_by_name_id(self, name_id, new_vector):
        for i in range(len(self.__vectors)):
            if self.__vectors[i].get_name_id() == name_id:
                self.__vectors[i] = new_vector
                return
        raise Exception("No vector with the given name_id")

    #delete a vector at a given index:
    def delete_vector(self, index):
        del self.__vectors[index]
        
    #delete a vector identified by name_id:
    def delete_vector_by_name_id(self, name_id):
        for i in range(len(self.__vectors)):
            if self.__vectors[i].get_name_id() == name_id:
                del self.__vectors[i]
                return
        raise Exception("No vector with the given name_id")
    
    #plot all vectors based on type and color with matplotlib (types: 1=circle, 2=square, 3=triangle, other = diamond):
    def plot_all(self):
        for vector in self.__vectors:
            if vector.get_type() == 1:
                plt.plot(vector.get_val(), str(vector.get_key())+'o')
            elif vector.get_type() == 2:
                plt.plot(vector.get_val(), str(vector.get_key())+'s')
            elif vector.get_type() == 3:
                plt.plot(vector.get_val(), str(vector.get_key())+'^')
            else:
                plt.plot(vector.get_val(), str(vector.get_key())+'D')
        plt.show()
        
    #get the list of vectors having the minimum less than a given value:
    def get_min_less_than(self, value):
        return [x for x in self.__vectors if x.min() < value]
    
    #delete all vectors for which the max value is equal to a given value:
    def delete_max_equal_to(self, value):
        self.__vectors = [x for x in self.__vectors if x.max() != value]
        
    #update the color of a vector identified by name id:
    def update_color_by_name_id(self, name_id, color):
        for i in range(len(self.__vectors)):
            if self.__vectors[i].get_name_id() == name_id:
                self.__vectors[i].set_color(color)
                return True
        raise Exception("No vector with the given name_id")
    
    #create a vector which represents the sum of all vectors in the repository:
    def create_sum_all(self):
        name_id = "sum"
        type = 1
        color = "r"
        val = []
        for vector in self.__vectors:
            val.append(vector.get_val())
        val = [sum(x) for x in zip(*val)]
        vector = MyVector(name_id, color, type, val)
        self.add_vector(vector)
        
    def clear(self):
        self.__vectors.clear()