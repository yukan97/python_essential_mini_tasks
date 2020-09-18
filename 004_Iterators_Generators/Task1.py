class MyReverseIter:
    
    def __init__(self, my_list):
        self.my_list = my_list
        self.step = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if -self.step > len(self.my_list):
            raise StopIteration
        else:
            element = self.my_list[self.step]
            self.step = self.step - 1
        return element
    
test_list = [1, 2, 3]

my_iter = MyReverseIter(test_list)

print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())

