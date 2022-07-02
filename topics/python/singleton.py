#Solution - 1

class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

obj1 = Singleton()
obj1.data = 5

print(obj1.data)
obj2 = Singleton()
print(obj2.data)
obj2.data = 10
print(obj1.data)

print(id(obj1))
print(id(obj2))