class Type(type):
    def __repr__(cls):
        return cls.__name__
class O(object):
    __metaclass__ = Type
class A(O):pass
class B(O):pass
class C(O):pass
class D(O):pass
class E(O):pass
class K1(A, B, C):pass
class K2(D, B, E):pass
class K3(D, A):pass
class Z(K1, K2, K3):pass

print(Z.__mro__)
