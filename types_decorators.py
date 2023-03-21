# Types of decorators

# 1. function decorator
print("Function Decorator :")
def f1(fn):
    def wrapper():
        print("Started")
        fn()
        print("Ended")        
    return wrapper

@f1
def f2():
    print("Hello, in function f2")
    
f2()

# 2. class decorator
print("\nClass Decorator :")
def cls_decorator(cls):
    cls.new_attr = "new attribute"
    return cls

@cls_decorator
class MyClass:
    attr = "old attribute"
    def my_method(self):
        print("Hello from MyClass")

obj = MyClass()
print(obj.attr)
print(obj.new_attr)
obj.my_method()
