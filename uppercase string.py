class Iostring():
    def __init__(self):
        self.str =""
    def Get_String(self):
        self.str = input("Enter string: ")
    def Print_String(self):
        self.str = print(f"Result = {self.str.upper()}")

Upper_string = Iostring()
Upper_string.Get_String()
Upper_string.Print_String()