def my_reverse(input_list):
    
    step = -1

    while -step <= len(input_list):
        yield input_list[step]
        step = step - 1
        
        
test_list = [1, 2, 3]

generator = my_reverse(test_list)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))