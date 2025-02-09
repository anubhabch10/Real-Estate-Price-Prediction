import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:   
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    arr = np.zeros(len(__data_columns))
    arr[0] = sqft
    arr[1] = bath
    arr[2] = bhk
    if loc_index >= 0:
        arr[loc_index] = 1

    return round(__model.predict([arr])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __data_columns
    global __locations

    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'artifacts', 'columns.json')
    with open(file_path, 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'artifacts', 'kolkata_home_prices_model.pickle')
    global __model
    with open(file_path, 'rb') as f:

        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Barasat',1000, 3, 3))
    print(get_estimated_price('Rajarhat',1000, 2, 2))
    print(get_estimated_price('Joka', 1000, 2, 2))
    print(get_estimated_price('New Town', 1000, 2, 2))