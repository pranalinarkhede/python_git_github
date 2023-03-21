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