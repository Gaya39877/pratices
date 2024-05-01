import pickle



#pickling
data = {"name":"gayathri","age":25}
filename = "dict.pickle"
with open(filename,"wb") as f:
    pickle.dump(data, f)

# unpickling
filename = "dict.pickle"
with open(filename, 'rb') as f :
    dict_data = pickle.load(f)

print(dict_data["age"])