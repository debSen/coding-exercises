class Parent():
    def __init__(self) -> None:
        print("In Parent's __init__")
        self.A = 0
    def parent_method(self):
        print("In parent method")


class Child(Parent):
    def __init__(self) -> None:
        # Super executes parent init method
        # Without this we only have access to other methods
        # Super is also useful for correct resolution of MRO in case of multiple inheritance
        super().__init__()

class GrandChild(Child):
    def __init__(self) -> None:
        super().__init__()


C = Child()
G = GrandChild()
C.parent_method()
G.parent_method()
print(isinstance(C, Parent))
print(isinstance(G, Parent))
print(issubclass(GrandChild, Parent))