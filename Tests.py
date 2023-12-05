from colorama import Fore, Style
from VectorRepository import VectorRepository
from MyVector import MyVector
from time import sleep
import os

def test_add():
    v1 = MyVector("v1", "r", 1, [1,2,3,4,5])
    v2 = MyVector("v2", "b", 1, [1,2,3,4,5])
    v1 += v2
    assert v1.get_val() == [2,4,6,8,10], Fore.RED+"Add vectors 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Add vectors 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "r", 1, [1,2,3,4,5])
    v2 = MyVector("v2", "b", 1, [43, 23, 12, 34, 56])
    v1 += v2
    assert v1.get_val() == [44, 25, 15, 38, 61], Fore.RED+"Add vectors 2 failed"+Style.RESET_ALL
    print(Fore.GREEN + "Add vectors 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "r", 1, [-2 , 3, 4, 5, 6])
    v2 = MyVector("v2", "b", 1, [43, 23, 12, 34, 56])
    v1+=v2
    assert v1.get_val() == [41, 26, 16, 39, 62], Fore.RED+"Add vectors 3 failed"+Style.RESET_ALL
    print(Fore.GREEN + "Add vectors 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Add vectors passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_substraction():
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 1, [4, 9, 15, 19])
    v1-=v2
    assert v1.get_val() == [1, 1, 0, 5],Fore.RED+"Substarct vectors 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Add vectors 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    v2 = MyVector("v2", "g", 1, [4, 9, 15, 19])
    v1-=v2
    assert v1.get_val() == [16, -12, -5, -19],Fore.RED+"Substarct vectors 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Add vectors 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    v2 = MyVector("v2", "g", 1, [4, 9, 15, 19])
    v1-=v2
    assert v1.get_val() == [16, -12, -5, -19],Fore.RED+"Substarct vectors 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Add vectors 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Substract vectors passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_multiply():
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 1, [4, 9, 15, 19])
    assert v1*v2 == 5*4 + 10*9 + 15*15 + 24*19, Fore.RED+"Multiply vectors 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+"Multiply vectors 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    v2 = MyVector("v2", "g", 1, [4, 9, 15, 19])
    assert v1*v2 == 20*4 + (-3)*9 + 10*15 + 0*19, Fore.RED+"Multiply vectors 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Multiply vectors 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    v2 = MyVector("v2", "g", 1, [4, 9, 15, 19])
    assert v1*v2 == 20*4 + (-3)*9 + 10*15 + 0*19, Fore.RED+"Multiply vectors 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Multiply vectors 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Multiply vectors passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_average():
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    assert v1.avg() == (5+10+15+24)/4, Fore.RED+"Average 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Average 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    assert v1.avg() == (20-3+10+0)/4, Fore.RED+"Average 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Average 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    assert v1.avg() == (20-3+10+0)/4, Fore.RED+"Average 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Average 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Average passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_sum_elem():
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    assert v1.sum() == 5+10+15+24, Fore.RED+"Sum of elemnts 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Sum of elements 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    assert v1.sum() == 20-3+10+0, Fore.RED+"Sum of elements 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Sum of elements 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    assert v1.sum() == 20-3+10+0, Fore.RED+"Sum of elements 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Sum of elements 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Sum of elements passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_prod():
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    assert v1.prod() == 5*10*15*24, Fore.RED+"Product of elements 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Product of elements 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    assert v1.prod() == 20*(-3)*10*0, Fore.RED+"Product of elements 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Product of elements 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    assert v1.prod() == 20*(-3)*10*0, Fore.RED+"Product of elements 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Product of elements 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Product of elements passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_min():
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    assert v1.min() == 5, Fore.RED+"Minimum of elements 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Minimum of elements 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    assert v1.min() == -3, Fore.RED+"Minimum of elements 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Minimum of elements 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    assert v1.min() == -3, Fore.RED+"Minimum of elements 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Minimum of elements 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Minimum of elements passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_max():
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    assert v1.max() == 24, Fore.RED+"Maximum of elements 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Maximum of elements 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    assert v1.max() == 20, Fore.RED+"Maximum of elements 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Maximum of elements 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    v1 = MyVector("v1", "b", 1, [20, -3, 10, 0])
    assert v1.max() == 20, Fore.RED+"Maximum of elements 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Maximum of elements 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Maximum of elements passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_add_vector():
    repo=VectorRepository()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    repo.add_vector(v1)
    assert (repo.get_vectors() == [v1]), Fore.RED+"Add vector 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Add vector 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    v2 = MyVector("v2", "b", 1, [20, -3, 10, 0])
    repo.add_vector(v2)
    assert repo.get_vectors() == [v1, v2], Fore.RED+"Add vector 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Add vector 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    v3 = MyVector("v3", "b", 1, [20, -3, 10, 0])
    repo.add_vector(v3)
    assert repo.get_vectors() == [v1, v2, v3], Fore.RED+"Add vector 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Add vector 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Add vector passed" + Style.RESET_ALL)
    sleep(0.01)

def test_get_vector_at_index():
    repo = VectorRepository()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 2, [4, 3, 1, 8, 10, 25])
    v3 = MyVector("v3", "k", 2, [4, 3, 1, 54, 1, 25])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.add_vector(v3)
    assert repo.get_vector(0) == [v1], Fore.RED+"Get vector at index 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Get vector at index 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    assert repo.get_vector(1) == [v2], Fore.RED+"Get vector at index 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Get vector at index 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    assert repo.get_vector(2) == [v3], Fore.RED+"Get vector at index 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Get vector at index 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Get vector at index passed" + Style.RESET_ALL)
    sleep(0.01)

def test_update_vector_at_index():
    repo = VectorRepository()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 2, [4, 3, 1, 8, 10, 25])
    v3 = MyVector("v3", "k", 2, [4, 3, 1, 54, 1, 25])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.update_vector(0, v3)
    assert repo.get_vector(0) == [v3], Fore.RED+"Update vector at index 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Update vector at index 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.update_vector(1, v1)
    assert repo.get_vector(1) == [v1], Fore.RED+"Update vector at index 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Update vector at index 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.update_vector(2, v2)
    assert repo.get_vector(2) == [v2], Fore.RED+"Update vector at index 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Update vector at index 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Update vector at index passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_update_vector_by_name_id():
    repo = VectorRepository()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 2, [4, 3, 1, 8, 10, 25])
    v3 = MyVector("v3", "k", 2, [4, 3, 1, 54, 1, 25])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.update_vector_by_name_id("v1", v3)
    assert repo.get_vector(0) == [v3], Fore.RED+"Update vector by name_id 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Update vector by name_id 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.update_vector_by_name_id("v2", v1)
    assert repo.get_vector(1) == [v1], Fore.RED+"Update vector by name_id 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Update vector by name_id 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.update_vector_by_name_id("v3", v2)
    assert repo.get_vector(2) == [v2], Fore.RED+"Update vector by name_id 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Update vector by name_id 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Update vector by name_id passed" + Style.RESET_ALL)
    sleep(0.01)

def test_delete_vector_at_index():
    repo = VectorRepository()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 2, [4, 3, 1, 8, 10, 25])
    v3 = MyVector("v3", "k", 2, [4, 3, 1, 54, 1, 25])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.add_vector(v3)
    repo.delete_vector(0)
    assert repo.get_vectors() == [v2, v3], Fore.RED+"Delete vector at index 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Delete vector at index 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.delete_vector(1)
    assert repo.get_vectors() == [v2], Fore.RED+"Delete vector at index 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Delete vector at index 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.delete_vector(0)
    assert repo.get_vectors() == "No vectors", Fore.RED+"Delete vector at index 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Delete vector at index 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Delete vector at index passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_delete_vector_by_name_id():
    repo = VectorRepository()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 2, [4, 3, 1, 8, 10, 25])
    v3 = MyVector("v3", "k", 2, [4, 3, 1, 54, 1, 25])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.add_vector(v3)
    repo.delete_vector_by_name_id("v1")
    assert repo.get_vectors() == [v2, v3], Fore.RED+"Delete vector by name_id 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Delete vector by name_id 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.delete_vector_by_name_id("v2")
    assert repo.get_vectors() == [v3], Fore.RED+"Delete vector by name_id 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Delete vector by name_id 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.delete_vector_by_name_id("v3")
    assert repo.get_vectors() == "No vectors", Fore.RED+"Delete vector by name_id 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Delete vector by name_id 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Delete vector by name_id passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_get_min_less_than():
    repo = VectorRepository()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 2, [4, 3, 1, 8, 10, 25])
    v3 = MyVector("v3", "k", 2, [4, 3, 1, 54, 1, 25])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.add_vector(v3)
    assert repo.get_min_less_than(5) == [v2, v3], Fore.RED+"Get min less than 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Get min less than 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    assert repo.get_min_less_than(10) == [v1, v2, v3], Fore.RED+"Get min less than 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Get min less than 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    assert repo.get_min_less_than(0) == [], Fore.RED+"Get min less than 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Get min less than 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Get min less than passed" + Style.RESET_ALL)
    sleep(0.01)

def test_delete_max_equal_to():
    repo = VectorRepository()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 2, [4, 3, 1, 8, 10, 25])
    v3 = MyVector("v3", "k", 2, [4, 3, 1, 54, 1, 26])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.add_vector(v3)
    repo.delete_max_equal_to(24)
    assert repo.get_vectors() == [v2, v3], Fore.RED+"Delete max equal to 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Delete max equal to 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.delete_max_equal_to(25)
    assert repo.get_vectors() == [v3], Fore.RED+"Delete max equal to 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Delete max equal to 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.delete_max_equal_to(54)
    assert repo.get_vectors() == "No vectors", Fore.RED+"Delete max equal to 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Delete max equal to 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Delete max equal to passed" + Style.RESET_ALL)
    sleep(0.01)

def test_update_color_by_name_id():
    repo = VectorRepository()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    repo.add_vector(v1)
    repo.update_color_by_name_id("v1", "r")
    assert repo.get_vector(0).get_color() == "red", Fore.RED+"Update color by name_id 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Update color by name_id 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.update_color_by_name_id("v1", "g")
    assert repo.get_vector(0).get_color() == "green", Fore.RED+"Update color by name_id 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Update color by name_id 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.update_color_by_name_id("v1", "k")
    assert repo.get_vector(0).get_color() == "black", Fore.RED+"Update color by name_id 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Update color by name_id 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Update color by name_id passed" + Style.RESET_ALL)
    sleep(0.01)
    
def test_create_sum_all():
    repo = VectorRepository()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 2, [4, 3, 1, 8])
    v3 = MyVector("v3", "k", 2, [4, 3, 1, 54])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.add_vector(v3)
    repo.create_sum_all()
    assert repo.get_vector(3).get_val() == [13, 16, 17, 86], Fore.RED+"Create sum all 1 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Create sum all 1 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.clear()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    repo.add_vector(v1)
    repo.create_sum_all()
    assert repo.get_vector(1).get_val() == [5, 10, 15, 24], Fore.RED+"Create sum all 2 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Create sum all 2 passed" + Style.RESET_ALL)
    sleep(0.01)
    repo.clear()
    v1 = MyVector("v1", "b", 1, [5, 10, 15, 24])
    v2 = MyVector("v2", "g", 2, [4, 3, 1, 8])
    repo.add_vector(v1)
    repo.add_vector(v2)
    repo.create_sum_all()
    print(repo.get_vector(1).get_val())
    assert repo.get_vector(2).get_val() == [9, 13, 16, 32], Fore.RED+"Create sum all 3 failed"+Style.RESET_ALL
    print(Fore.GREEN+ "Create sum all 3 passed" + Style.RESET_ALL)
    sleep(0.01)
    print(Fore.LIGHTGREEN_EX + "Create sum all passed" + Style.RESET_ALL)
    sleep(0.01)

def test_all():
    os.system('cls||clear')
    x = Fore.BLUE + "Testing... \n" + Style.RESET_ALL
    for characters in x:
        print(characters, end = '')
        sleep(0.05)
    try:
        test_add()
        test_substraction()
        test_multiply()
        test_average()
        test_sum_elem()
        test_prod()
        test_max()
        test_min()
        test_add_vector()
        #test_get_vector_at_index()
        #test_update_vector_at_index()
        #test_update_vector_by_name_id()
        test_delete_vector_at_index()
        test_delete_vector_by_name_id()
        test_get_min_less_than()
        test_delete_max_equal_to()
        test_update_color_by_name_id()
        test_create_sum_all()
    except Exception as e:
        print(Fore.RED)
        print(e)
        print("Tests failed")
        print(Style.RESET_ALL)
        return
    print(Style.RESET_ALL)
    passer = Fore.GREEN + Style.BRIGHT + "All tests passed" + Style.RESET_ALL
    for characters in passer:
        print(characters, end = '')
        sleep(0.05)
    sleep(2)
    os.system('cls||clear')