import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)

person_obj = Person("gayathri",25)

#pickling
# file_name = "class.pickle"
# with open(file_name, "wb") as f:
#     pickle.dump(person_obj, f)


#unpickling
file_name = "class.pickle"
with open(file_name, 'rb') as f :
    class_data = pickle.load(f)

class_data.display()