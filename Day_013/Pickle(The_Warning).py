import pickle

with open('Pickle.pkl', 'wb') as f: pickle.dump([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], f)

with open('Pickle.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)