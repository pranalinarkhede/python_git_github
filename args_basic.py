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
        
         
c = argsBasic()
c.adder(5,5,5)
c.multiplier(5,5,5)