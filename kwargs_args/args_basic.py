class argsBasic():
    def adder(self, *args):   
        sum = 0
        
        for n in args:
            sum = sum + n

        print("Sum:",sum)
        
    def multiplier(self, *args):
        mul = 1
        
        for n in args:
            mul = mul * n

        print("Multiplication:",mul)
        
    
    def toList(self, *args):
        lst = []
        
        print("List generated:",list(args))
        
             
c = argsBasic()
c.adder(5,45,89, 12, 47, 82)
c.multiplier(3, 67, 88)
c.toList('apple','grapes','pineapple','pear','mango')