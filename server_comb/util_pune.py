import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price_pune(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    p = np.zeros(len(__data_columns))
    p[0] = sqft
    p[1] = bath
    p[2] = bhk

    if loc_index >= 0:
        p[loc_index] = 1

    return round(__model.predict([p])[0], 2)

def get_location_names_pune():
    return __locations

def load_saved_artifacts_pune():
    global __data_columns
    global __locations
    global __model

    with open("./artifacts_pune/columns_pune.json", 'r') as f:
        __data_columns = json.load(f)['data_columns_pune']
        __locations = __data_columns[3:]  # Extracting location names from data_columns

    if __model is None:
        with open("./artifacts_pune/pune_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)

if __name__ == '__main__':
    load_saved_artifacts_pune()
    print(get_location_names_pune())
    print(__data_columns)
    print(__locations)

    print(get_estimated_price_pune('Laxmi Road', 4000, 4, 2))
