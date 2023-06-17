class Destructor:
    def __init__(self):
        print("this is constructor")
    def __del__(self):
        print("this is destructor")
    def function1():
        d1=Destructor()
    def function2():
        d2=Destructor()
        print('calling function1')
        function1()
        print('calling function2')
        function2()
