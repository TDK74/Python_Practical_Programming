def deco(f):
    print("my_func is running")
    return f
@deco
def my_func(x):
    return x * 2

print(my_func(5))
