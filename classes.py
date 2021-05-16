class X:
    def __init__(self,name):
        self.name = name
        print(name)
    def shutdown(self):
        print(self.name)
        self.__del__()
    def execute(self,dictionary):
        print(self.name)
        for keys,values in dictionary.values():
            print(f"{keys},{values}")
class A(X):
    def __init__(self, name):
        self.clas = "Class: A"
        print("Class: A")
        super().__init__(name)
    def execute(self, dictionary):
        print(self.clas)
        return super().execute(dictionary)
    def shutdown(self):
        print(self.clas)
        return super().shutdown()
class B(X):
    def __init__(self, name):
        self.clas = "Class: B"
        print("Class: B")
        super().__init__(name)
    def execute(self, dictionary):
        print(self.clas)
        return super().execute(dictionary)
    def shutdown(self):
        print(self.clas)
        return super().shutdown()
class C(X):
    def __init__(self, name):
        self.clas = "Class: C"
        print("Class: C")
        super().__init__(name)
    def execute(self, dictionary):
        print(self.clas)
        return super().execute(dictionary)
    def shutdown(self):
        print(self.clas)
        return super().shutdown()
Flag = "run"
while True:
    Flag = input()
    if Flag.lower() == "quit":
        break
    eval(Flag)
    pass