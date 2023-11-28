from VectorRepository import VectorRepository
from MyVector import MyVector

def test_add_vectors():
    v1 = MyVector("v1", "red", 1, [1,2,3,4,5])
    v2 = MyVector("v2", "blue", 2, [1,2,3,4,5])
    v1 += v2
    assert v1.get_val() == [2,4,6,8,10]
