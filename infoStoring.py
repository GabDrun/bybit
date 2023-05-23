import pickle
import os

path = 'db/'

def save(name, obj):
    if type(obj).__name__ not in ['InstrumentsInfo', 'KlinesInfo']:
        print('Warning: object class is not supported')
        print('Try: InstrumentsInfo or KlinesInfo')
        return
    with open(path + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f)


def load(name):
    with open(path + name + '.pkl', 'rb') as f:
        return pickle.load(f).reset_session()
    

def load_all():
    files = os.listdir(path)
    files = [file for file in files if file.endswith('.pkl')]
    return [load(file[:-4]) for file in files]
