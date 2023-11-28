from VectorRepository import VectorRepository
from MyVector import MyVector

def print_menu():
    print("1. Add a vector")
    print("2. Get a vector at a given index")
    print("3. Update a vector at a given index")
    print("4. Update a vector identified by name_id")
    print("5. Delete a vector at a given index")
    print("6. Delete a vector identified by name_id")
    print("7. Plot all vectors")
    print("0. Exit")
def UI():
        V = VectorRepository()
        print("Welcome to the Vector Manager!")
        #add some vectors for testing purposes:
        V.add_vector(MyVector("v1", "red", 1, [1,2,3,4,5]))
        while True:
            print_menu()
            print("\n")
            print(V.get_vectors())
            print("\n")
            option = int(input("Enter your option: "))
            if option == 1:
                name_id = str(input("Enter the name_id: "))
                type = int(input("Enter the type: "))
                color = input("Enter the color: ")
                val = input("Enter the values: ")
                val = val.split()
                val = [int(x) for x in val]
                vector = MyVector(name_id, color, type, val)
                V.add_vector(vector)
            elif option == 2:
                index = int(input("Enter the index: "))
                print(V.get_vector(index))
            elif option == 3:
                index = int(input("Enter the index: "))
                name_id = input("Enter the name_id: ")
                type = int(input("Enter the type: "))
                color = input("Enter the color: ")
                val = input("Enter the values: ")
                val = val.split()
                val = [int(x) for x in val]
                vector = MyVector(name_id, color, type, val)
                V.update_vector(index, vector)
            elif option == 4:
                name_id = input("Enter the name_id: ")
                type = int(input("Enter the type: "))
                color = input("Enter the color: ")
                val = input("Enter the values: ")
                val = val.split()
                val = [int(x) for x in val]
                vector = MyVector(name_id, color, type, val)
                V.update_vector_by_name_id(name_id, vector)
            elif option == 5:
                index = int(input("Enter the index: "))
                V.delete_vector(index)
            elif option == 6:
                name_id = input("Enter the name_id: ")
                V.delete_vector_by_name_id(name_id)
            elif option == 7:
                V.plot_all()
            elif option == 0:
                print("Thank you for using the Vector Manager!")
                break