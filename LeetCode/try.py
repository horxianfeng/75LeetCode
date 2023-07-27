aList = [[10, 20], [30, 40]]
bList = [10, 20, 30, 40]


print (aList[1])
print (bList.index(10))
print (bList[2:])
print (bList.index(20))
print (20 in bList[1:])

class Test() :
    def __init__(self, price) -> None:
        """
        :type price: list[int]
        """
        print(price)
        self.high = 50
    
    def func (self):
        sohai = 10
        print("haha")
        

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

t = Test(123)
# t.func()
