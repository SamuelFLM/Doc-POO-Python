class A:
    
    def m1(self):
        print("Metodo de A")


class B(A):
    def m2(self):
        print("Metodo de A")
        
class C(A):
    def m2(self):
        print("Metodo de A")


class D(B, C):
    pass