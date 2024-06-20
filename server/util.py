import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    a = np.zeros(len(__data_columns))
    a[0] = sqft
    a[1] = bath
    a[2] = bhk

    if loc_index >= 0:
        a[loc_index] = 1

    return round(__model.predict([a])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # Extracting location names from data_columns

    if __model is None:
        with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(__data_columns)
    print(__locations)

    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
