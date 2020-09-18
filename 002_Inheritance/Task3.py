class A:
    pass

class B(A):
    pass

class C(A):
    pass

#D(A, B) = Cannot create a consistent method resolution order (MRO) for bases A, B
class D(B, A):
    pass

class E(C, D):
    pass


print(E.__mro__)
print(D.__mro__)
print(C.__mro__)