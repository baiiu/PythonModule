class A:
    age = 1
    __age = 2

    def __init__(self):
        self.__age = 9

    def get_age(self):
        return self.__age

a = A();
print(a.get_age())
print(a.age)
print(A.age)

a.age = 'Hello'
print(a.age)
del a.age
print(a.age) # 实例属性被删除后，使用类属性
