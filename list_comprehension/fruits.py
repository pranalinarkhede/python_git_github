# list comprehension functionality:
class FruitBucket():
    def __init__(self):
        self.fruits = ["apple", "banana", "kiwi", "pine", "mango", 'pomogranate']

    def filterFruitsBy(self, char):
        new_fruit = [ x for x in self.fruits if char in x ]
        print(new_fruit)
    
f = FruitBucket()

f.filterFruitsBy('a')
f.filterFruitsBy('z')
f.filterFruitsBy('g')