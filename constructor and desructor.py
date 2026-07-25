class employee():
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        print("Desructor called")

def create_obj():
    print("Making oject")
    obj = employee()
    print("Function end")
    return obj

print("Calling Create_obj() function...")
obj = create_obj()
print("function ended")
