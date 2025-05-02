import pickle

def load_model():
    with open('app/model.pkl', 'rb') as f:
        model = pickle.load(f)

    return model