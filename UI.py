import sys
from VectorRepository import VectorRepository
from MyVector import MyVector
from colorama import Fore, Style
from os import system
from time import sleep

def print_menu():
    print(Fore.YELLOW)
    print("1. Add a vector")
    print("2. Get a vector at a given index")
    print("3. Update a vector at a given index")
    print("4. Update a vector identified by name_id")
    print("5. Delete a vector at a given index")
    print("6. Delete a vector identified by name_id")
    print("7. Plot all vectors")
    print("8. Get the list of vectors having the minimum less than a given value")
    print("9. Delete all vectors having the maximum equal to a given value")
    print("10. Update the color of a vector identified by name_id")
    print("11. Create a vector representing the sum of all the vectors in the repository")
    print("0. Exit")
    print(Style.RESET_ALL)
    
V = VectorRepository()
#globals so they don't get reset when the fucncton gets recalled after an error
V.add_vector(MyVector("v1", "r", 1, [1,2,3,4,5]))
V.add_vector(MyVector("v2", "g", 2, [12 , 23, 34, 45, 56]))

def UI():
    try:
        while True:
            print_menu()
            print("\n")
            print(V.get_vectors())
            print("\n")
            option = int(input("Enter your option: "))
            system('cls||clear')
            if option == 1:
                name_id = str(input("Enter the name_id: "))
                if name_id == "":
                    raise ValueError("Invalid name_id")
                type = int(input("Enter the type: "))
                color = input("Choose the color between r, g, b, c, m, y, k, w: ")
                if color not in ["r", "g", "b", "c", "m", "y", "k", "w"]:
                    raise Exception("Invalid color")
                val = input("Enter the values: ")
                val = val.split()
                for elem in val:
                    if not elem.isnumeric():
                        raise ValueError("Values can only be integers")
                val = [int(x) for x in val]
                vector = MyVector(name_id, color, type, val)
                V.add_vector(vector)
                system("cls||clear")
            elif option == 2:
                index = int(input("Enter the index: "))
                system("cls||clear")
                print(V.get_vector(index))
                print("\n")
                x = "Press Enter to continue... "
                for character in x:
                    print(character, end='')
                    sleep(0.01)
                wait = input()
                system("cls||clear")
            elif option == 3:
                index = int(input("Enter the index: "))
                name_id = input("Enter the name_id: ")
                type = int(input("Enter the type: "))
                color = input("Choose the color between r, g, b, c, m, y, k, w: ")
                if color not in ["r", "g", "b", "c", "m", "y", "k", "w"]:
                    raise ValueError("Invalid color")
                val = input("Enter the values: ")
                val = val.split()
                val = [int(x) for x in val]
                vector = MyVector(name_id, color, type, val)
                V.update_vector(index, vector)
                system("cls||clear")
            elif option == 4:
                name_id = input("Enter the name_id: ")
                type = int(input("Enter the type: "))
                color = input("Choose the color between r, g, b, c, m, y, k, w: ")
                if color not in ["r", "g", "b", "c", "m", "y", "k", "w"]:
                    raise ValueError("Invalid color")
                val = input("Enter the values: ")
                val = val.split()
                val = [int(x) for x in val]
                vector = MyVector(name_id, color, type, val)
                V.update_vector_by_name_id(name_id, vector)
                system("cls||clear")
            elif option == 5:
                index = int(input("Enter the index: "))
                V.delete_vector(index)
            elif option == 6:
                name_id = input("Enter the name_id: ")
                V.delete_vector_by_name_id(name_id)
            elif option == 7:
                system("cls||clear")
                V.plot_all()
            elif option == 0:
                sleep(1)
                print("\n")
                x = "Press Enter to exit... "
                for character in x:
                    print(character, end='')
                    sleep(0.01)
                wait = input()
                system("cls||clear")
                break
            elif option == 8:
                minimum = int(input("Enter the minimum: "))
                system('cls||clear')
                print(V.get_min_less_than(minimum))
                print("\n")
                x = "Press Enter to exit... "
                for character in x:
                    print(character, end='')
                wait = input()
                system("cls||clear")
            elif option == 9:
                maximum = int(input("Enter the maximum: "))
                system('cls||clear')
                V.delete_max_equal_to(maximum)
            elif option == 10:
                name_id = input("Enter the name_id: ")
                color = input("Choose the color between r, g, b, c, m, y, k, w: ")
                if color not in ["r", "g", "b", "c", "m", "y", "k", "w"]:
                    raise ValueError("Invalid color")
                V.update_color_by_name_id(name_id, color)
            elif option == 11:
                V.create_sum_all()
            elif option<0 or option>11 or option!=int:
                raise ValueError("Invalid option")
        system("cls||clear")
    except Exception as ex:
        system("cls||clear")
        print(Fore.RED)
        print(ex)
        print(Style.RESET_ALL)
        print("\n\n")
        sleep(2)
        system("cls||clear")
        UI()
    except:
        system("cls||clear")
        print(Fore.RED)
        print("Something went wrong \n\n")
        print(Style.RESET_ALL)
        sleep(2)
        system("cls||clear")
        UI()