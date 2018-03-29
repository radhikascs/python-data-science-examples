
def absolute_value(num):
    if num >=0:
        return num
    else:
        return -num

print(absolute_value(2))

def greet(*names):
    #This function greets all the person in the names tuple

    for name in names:
        print("Hello "+name)


greet("Monica","Luke","Steve","John")