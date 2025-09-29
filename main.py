import os
base_path = os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_path, "test/file.txt")

f=open(file_path,"r")
read_file=f.read()
print(read_file)


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_info(self):
        self.college="ABC"
darshna=Student("Darshna",20)
darshna.display_info()
print(f"Name: {darshna.name}, Age: {darshna.age}")
print(f"College: {darshna.college}")
