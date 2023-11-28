from MyVector import MyVector
from matplotlib import pyplot as plt

class VectorRepository:
    def __init__(self):
        self.__vectors = []
        
    def add_vector(self, vector):
        self.__vectors.append(vector)
        
    def get_vectors(self):
        return self.__vectors
    
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
                plt.plot(vector.get_val(), str(vector.get_color()) + 'o')
            elif vector.get_type() == 2:
                plt.plot(vector.get_val(), 'bs')
            elif vector.get_type() == 3:
                plt.plot(vector.get_val(), 'g^')
            else:
                plt.plot(vector.get_val(), 'kD')
        plt.show()