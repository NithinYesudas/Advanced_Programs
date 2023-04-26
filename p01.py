# Every class in python inherits from the object class
# In python there is a concept called duck typing

class FirstClass: 

    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y

   
    def __add__(self, other): # Overloading the + operator
        temp = FirstClass()

        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp

    def __contains__(self, item): # Overloading the in operator
        return item in self.x

    def display(self): 
        print(self.x,self.y)


def hello():
    print("Hello World")


if __name__ == '__main__': # This is the main function
    hello()
    f = FirstClass(10,15)
    g = FirstClass(4,8)
    z = f + g
    z.display()
